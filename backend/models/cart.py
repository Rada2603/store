import pandas as pd
import json
from fastapi import HTTPException
from utils import Product


def view_cart():
    cart_csv = pd.read_csv(r"data\korpa.csv")
    cart_json = cart_csv.to_json(orient="records")
    return json.loads(cart_json)


def add_cart(product: Product):
    korpa = pd.read_csv(r"data\korpa.csv")
    prodavnica = pd.read_csv(r"data\prodavnica.csv")
    if product.naziv in prodavnica["Naziv"].values:
        if (
            int(product.kolicina)
            <= prodavnica.loc[prodavnica["Naziv"] == product.naziv, "Kolicina"].values[
                0
            ]
        ):
            prodavnica.loc[prodavnica["Naziv"] == product.naziv, "Kolicina"] -= int(
                product.kolicina
            )
            prodavnica.to_csv(r"data\prodavnica.csv", index=False)
        else:
            raise HTTPException(status_code=400, detail="Pogrešan kolicina")
        if product.naziv in korpa["Naziv"].values:
            korpa.loc[korpa["Naziv"] == product.naziv, "Kolicina"] += int(
                product.kolicina
            )
            korpa.to_csv(r"data\korpa.csv", index=False)
        else:
            prodavnica = pd.read_csv(r"data\prodavnica.csv")
            store_cena = prodavnica.loc[
                prodavnica["Naziv"] == product.naziv, "Cena"
            ].values[0]
            novi_proizvod = {
                "Naziv": product.naziv,
                "Cena": store_cena,
                "Kolicina": product.kolicina,
            }
            korpa = korpa._append(novi_proizvod, ignore_index=True)
            korpa.to_csv(r"data\korpa.csv", index=False)
    else:
        raise HTTPException(status_code=400, detail="Pogrešan proizvod")
    return korpa.to_dict(orient="records"), prodavnica.to_dict(orient="records")


def delete_product_cart(product: Product):
    korpa = pd.read_csv(r"data\korpa.csv")
    prodavnica = pd.read_csv(r"data\prodavnica.csv")

    if product.naziv not in korpa["Naziv"].values:
        raise HTTPException(status_code=400, detail="Pogrešan proizvod")
    cart_kolicina = korpa.loc[korpa["Naziv"] == product.naziv, "Kolicina"].values[0]
    if int(product.kolicina) > cart_kolicina:
        raise HTTPException(status_code=400, detail="Pogrešan kolicina")

    if int(product.kolicina) == cart_kolicina:
        korpa = korpa[korpa["Naziv"] != product.naziv]
    else:
        korpa.loc[korpa["Naziv"] == product.naziv, "Kolicina"] -= int(product.kolicina)
    korpa.to_csv(r"data\korpa.csv", index=False)
    prodavnica.loc[prodavnica["Naziv"] == product.naziv, "Kolicina"] += int(
        product.kolicina
    )
    prodavnica.to_csv(r"data\prodavnica.csv", index=False)
    return korpa.to_dict(orient="records"), prodavnica.to_dict(orient="records")
