import pandas as pd
import json
from utils import User, Product
from fastapi import HTTPException

store_path = r"data\prodavnica.csv"
ulogovani_prodavci = r"data\ulogovani_prodavci.json"


def view_store():
    store_csv = pd.read_csv(store_path)
    store_json = store_csv.to_json(orient="records")
    return json.loads(store_json)


"""Dodavanje novog proizvoda u prodavnicu"""


def add_new_product_in_store(seller: User, product: Product):
    with open(ulogovani_prodavci, "r") as f:
        seler_log = json.load(f)
        for seler in seler_log:
            if (
                seler["username"] == seller.username
                and seler["password"] == seller.password
            ):
                prodavnica = pd.read_csv(store_path)
                new_product = {
                    "Naziv": product.naziv,
                    "Cena": product.cena,
                    "Kolicina": product.kolicina,
                }
                if product.naziv not in prodavnica["Naziv"].values:
                    prodavnica = prodavnica._append(new_product, ignore_index=True)
                    prodavnica.to_csv(store_path, index=False)

                else:
                    raise HTTPException(
                        status_code=400, detail="Proizvod postoji u prodavnici"
                    )
        return {"Poruka": "Nemate dozvolu za menjanje prodavnice"}


"""Promena kolicine proizvoda"""


def change_quantity_product_in_store(seller: User, product: Product):
    with open(ulogovani_prodavci, "r") as f:
        seler_log = json.load(f)
        for seler in seler_log:
            print("????")
            if (
                seler["username"] == seller.username
                and seler["password"] == seller.password
            ):
                prodavnica = pd.read_csv(store_path)
                if product.naziv in prodavnica["Naziv"].values:
                    prodavnica.loc[
                        prodavnica["Naziv"] == product.naziv, "Kolicina"
                    ] += int(product.kolicina)
                    prodavnica.to_csv(store_path, index=False)
                    return {"Poruka": "Količina proizvoda je ažurirana u prodavnici"}
                else:
                    raise HTTPException(status_code=400, detail="Pogrešan proizvod")
        return {"Poruka": "Nemate dozvolu za menjanje prodavnice"}
