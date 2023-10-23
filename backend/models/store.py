import pandas as pd
import json
from utils import Seller, Product


def view_store():
    store_csv = pd.read_csv(r"data\prodavnica.csv")
    store_json = store_csv.to_json(orient="records")
    return json.loads(store_json)


def change_store(seller: Seller, product: Product):
    with open(r"data\ulogovani_prodavci.json", "r") as f:
        seler_log = json.load(f)
        for seler in seler_log:
            if (
                seler["username"] == seller.username
                and seler["password"] == seller.password
            ):
                prodavnica = pd.read_csv(r"data\prodavnica.csv")
                new_product = {
                    "Naziv": product.naziv,
                    "Cena": product.cena,
                    "Kolicina": product.kolicina,
                }
                if product.naziv not in prodavnica["Naziv"].values:
                    print(product.naziv)
                    prodavnica = prodavnica._append(new_product, ignore_index=True)

                else:
                    prodavnica.loc[
                        prodavnica["Naziv"] == product.naziv, "Kolicina"
                    ] += int(product.kolicina)
                prodavnica.to_csv(r"data\prodavnica.csv", index=False)
        return {"Nemate dozvolu za menjanje prodavnice"}