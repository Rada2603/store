import pandas as pd
from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel
import uvicorn
from pydantic import BaseModel

app = FastAPI()
class Product(BaseModel):
    naziv: str
    kolicina: int


@app.get("/store")
def view_store():
    store_csv = pd.read_csv(r"data\prodavnica.csv")
    store_json = store_csv.to_json(orient="records")
    return json.loads(store_json)


@app.get("/cart")
def view_cart():
    cart_csv = pd.read_csv(r"data\korpa.csv")
    cart_json = cart_csv.to_json(orient="records")
    return json.loads(cart_json)


@app.post("/add_product")
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
            korpa.loc[korpa["Naziv"] == product.naziv, "Kolicina"] += int(product.kolicina)
            korpa.to_csv(r"data\korpa.csv", index=False)
        else:
            prodavnica = pd.read_csv(r"data\prodavnica.csv")
            store_cena = prodavnica.loc[
                prodavnica["Naziv"] == product.naziv, "Cena"
            ].values[0]
            novi_proizvod = {
                "Naziv": product.naziv,
                "Cena": store_cena,
                "Kolicina":product.kolicina,
            }
            korpa = korpa._append(novi_proizvod, ignore_index=True)
            korpa.to_csv(r"data\korpa.csv", index=False)
    else:
        raise HTTPException(status_code=400, detail="Pogrešan proizvod")
    return korpa.to_dict(orient="records"), prodavnica.to_dict(orient="records")


@app.post("/change_cart")
def delete_product_cart(product: Product):
    korpa = pd.read_csv(r"data\korpa.csv")
    prodavnica = pd.read_csv(r"data\prodavnica.csv")
    if product.naziv in korpa["Naziv"].values:
        print(product.naziv)
        cart_kolicina = korpa.loc[korpa["Naziv"] == product.naziv, "Kolicina"].values[0]
        if int(product.kolicina) < cart_kolicina:
            prodavnica.loc[prodavnica["Naziv"] == product.naziv, "Kolicina"] += int(product.kolicina)
            korpa.loc[korpa["Naziv"] == product.naziv, "Kolicina"] -= int(product.kolicina)
            prodavnica.to_csv(r"data\prodavnica.csv", index=False)
            korpa.to_csv(r"data\korpa.csv", index=False)
        elif int(product.kolicina) == cart_kolicina:
            prodavnica.loc[prodavnica["Naziv"] == product.naziv, "Kolicina"] += int(product.kolicina)
            korpa = korpa[korpa["Naziv"] != product.naziv]
            prodavnica.to_csv(r"data\prodavnica.csv", index=False)
            korpa.to_csv(r"data\korpa.csv", index=False)
        else:
            raise HTTPException(status_code=400, detail="Pogrešan kolicina")
    else:
        raise HTTPException(status_code=400, detail="Pogrešan proizvod")
    return korpa.to_dict(orient="records"), prodavnica.to_dict(orient="records")




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
