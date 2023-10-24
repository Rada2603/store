import pandas as pd
import json
from fastapi import HTTPException
from utils import Product, User

stefanova_korpa = r"data\korpa_stefan.csv"
oliverina_korpa = r"/data/oliverina_korpa.csv"
prodavnica = r"data\prodavnica.csv"


def view_cart_stefan():
    stefan_csv = pd.read_csv(stefanova_korpa)
    stefan_json = stefan_csv.to_json(orient="records")
    return json.loads(stefan_json)


def view_cart_olivera():
    olivera_csv = pd.read_csv(oliverina_korpa)
    olivera_json = olivera_csv.to_json(olivera_csv)
    return json.loads(olivera_json)


def add_product_stefancart(kupac: User, product: Product):
    stefan_csv = pd.read_csv(stefanova_korpa)
    with open(r"data\ulogovani_kupci.json") as f:
        kupac_log = json.load(f)
        for kupac1 in kupac_log:
            if (
                kupac1["username"] == kupac.username
                and kupac1["password"] == kupac.password
            ):
                prodavnica_csv = pd.read_csv(prodavnica)
                if product.naziv in prodavnica_csv["Naziv"].values:
                    if (
                        int(product.kolicina)
                        <= prodavnica_csv.loc[
                            prodavnica_csv["Naziv"] == product.naziv, "Kolicina"
                        ].values[0]
                    ):
                        
                        prodavnica_csv.loc[
                            prodavnica_csv["Naziv"] == product.naziv, "Kolicina"
                        ] -= int(product.kolicina)
                        prodavnica_csv.to_csv(prodavnica, index=False)
                    else:
                        raise HTTPException(status_code=400, detail="Pogrešna kolicina")
                    if product.naziv in stefan_csv["Naziv"].values:
                        stefan_csv.loc[
                            stefan_csv["Naziv"] == product.naziv, "Kolicina"
                        ] += int(product.kolicina)
                        stefan_csv.to_csv(stefanova_korpa, index=False)
                    else:
                        novi_proizvod = {
                            "Naziv": product.naziv,
                            "Cena": product.cena,
                            "Kolicina": product.kolicina,
                        }
                        stefan_csv = stefan_csv._append(
                            novi_proizvod, ignore_index=True
                        )
                        stefan_csv.to_csv(stefanova_korpa, index=False)
                else:
                    raise HTTPException(status_code=400, detail="Pogrešan proizvod")
            return stefan_csv.to_dict(orient="records"), prodavnica_csv.to_dict(
                orient="records"
            )
        return {"mesage": "Nemate dozvolu ya dodavanje proizvoda"}


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
