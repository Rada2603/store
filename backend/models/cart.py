import pandas as pd
import json
from fastapi import HTTPException
from utils import Product, User

prodavnica = r"data\prodavnica.csv"


def add_product(kupac: User, product: Product):
    with open(r"data\ulogovani_kupci.json") as f:
        kupac_log = json.load(f)
        kupac_ulogovani = False
        for kupac1 in kupac_log:
            if (
                kupac1["username"] == kupac.username
                and kupac1["password"] == kupac.password
            ):
                kupac_ulogovani = True
                break
        if not kupac_ulogovani:
            raise HTTPException(status_code=401, detail="Kupac nije ulogovan.")

    korpa = pd.read_csv(rf"data/{kupac.username}_korpa.csv")
    prodavnica_csv = pd.read_csv(prodavnica)

    if product.naziv not in prodavnica_csv["Naziv"].values:
        raise HTTPException(status_code=400, detail="Pogrešan proizvod")

    if (
        int(product.kolicina)
        > prodavnica_csv.loc[
            prodavnica_csv["Naziv"] == product.naziv, "Kolicina"
        ].values[0]
    ):
        raise HTTPException(status_code=400, detail="Pogrešna količina")

    if product.naziv in korpa["Naziv"].values:
        korpa.loc[korpa["Naziv"] == product.naziv, "Kolicina"] += int(product.kolicina)

    else:
        novi_proizvod = {
            "Naziv": product.naziv,
            "Cena": product.cena,
            "Kolicina": product.kolicina,
        }
        korpa = korpa._append(novi_proizvod, ignore_index=True)
    prodavnica_csv.loc[prodavnica_csv["Naziv"] == product.naziv, "Kolicina"] -= int(
        product.kolicina
    )
    prodavnica_csv.to_csv(prodavnica, index=False)
    korpa.to_csv(rf"data/{kupac.username}_korpa.csv", index=False)
    return korpa.to_dict(orient="records"), prodavnica_csv.to_dict(orient="records")


def delete_product(kupac: User, product: Product):
    with open(r"data\ulogovani_kupci.json") as f:
        kupac_log = json.load(f)
        kupac_ulogovani = False
        for kupac1 in kupac_log:
            if (
                kupac1["username"] == kupac.username
                and kupac1["password"] == kupac.password
            ):
                kupac_ulogovani = True
                break
        if not kupac_ulogovani:
            raise HTTPException(status_code=401, detail="Kupac nije ulogovan.")

    korpa = pd.read_csv(rf"data/{kupac.username}_korpa.csv")
    prodavnica_csv = pd.read_csv(prodavnica)

    if product.naziv not in korpa["Naziv"].values:
        raise HTTPException(status_code=400, detail="Pogrešan proizvod")
    if (
        int(product.kolicina)
        > korpa.loc[korpa["Naziv"] == product.naziv, "Kolicina"].values[0]
    ):
        raise HTTPException(status_code=400, detail="Pogrešna količina")
    if (
        int(product.kolicina)
        < korpa.loc[korpa["Naziv"] == product.naziv, "Kolicina"].values[0]
    ):
        korpa.loc[korpa["Naziv"] == product.naziv, "Kolicina"] -= int(product.kolicina)
    if (
        int(product.kolicina)
        == korpa.loc[korpa["Naziv"] == product.naziv, "Kolicina"].values[0]
    ):
        korpa = korpa[korpa["Naziv"] != product.naziv]
    prodavnica_csv.loc[prodavnica_csv["Naziv"] == product.naziv, "Kolicina"] += int(
        product.kolicina
    )
    prodavnica_csv.to_csv(prodavnica, index=False)
    korpa.to_csv(rf"data/{kupac.username}_korpa.csv", index=False)
    return korpa.to_dict(orient="records"), prodavnica_csv.to_dict(orient="records")
