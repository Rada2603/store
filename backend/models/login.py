from fastapi import HTTPException
from utils import User
import json
import pandas as pd

prodavci = r"data\prodavci.csv"
ulogovani_prodavci = r"data\ulogovani_prodavci.json"
kupci = r"data\kupci.csv"
ulogovani_kupci = r"data\ulogovani_kupci.json"


def login_seller(seller: User):
    seller_log = pd.read_csv(prodavci)
    if seller.username not in seller_log["Username"].values:
        raise HTTPException(status_code=400, detail="Seller not found")
    seller_password = seller_log.loc[
        seller_log["Username"] == seller.username, "Password"
    ].values[0]
    print(seller_password, seller.password)
    if seller.password != seller_password:
        raise HTTPException(status_code=400, detail="Wrong password")
    else:
        print(":::::")
        with open(ulogovani_prodavci, "r") as f:
            seler_json = json.load(f)
            for logged_seller in seler_json:
                if logged_seller["username"] == seller.username:
                    raise HTTPException(
                        status_code=400, detail="Prodavac je već ulogovan"
                    )
        seller_json = {"username": seller.username, "password": seller.password}
        seler_json.append(seller_json)
        with open(ulogovani_prodavci, "w") as f:
            json.dump(seler_json, f, indent=6)
        return {"message": "Uspesno ste ulogovani"}


def login_customer(customer: User):
    login_customer = pd.read_csv(kupci)
    if customer.username not in login_customer["Username"].values:
        raise HTTPException(status_code=400, detail="Pogresan kupac")
    customer_password = login_customer.loc[
        login_customer["Username"] == customer.username, "Password"
    ].values[0]
    print(customer_password, customer.password)
    if customer.password != customer_password:
        raise HTTPException(status_code=400, detail="Pogresna lozinka")
    else:
        with open(ulogovani_kupci, "r") as f:
            customer_json = json.load(f)
            print("::::")
            for logged_customer in customer_json:
                if logged_customer["username"] == customer.username:
                    raise HTTPException(
                        status_code=400, detail="Prodavac je već ulogovan"
                    )
        custommer_json = {"username": customer.username, "password": customer.password}
        customer_json.append(custommer_json)
        with open(ulogovani_kupci, "w") as f:
            json.dump(customer_json, f, indent=6)
        return {"message": "Dobro dosli"}
