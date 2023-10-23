from fastapi import HTTPException
from utils import Seller
import json
import pandas as pd


def login_seller(seller: Seller):
    seller_log = pd.read_csv(r"data\prodavci.csv")
    if seller.username not in seller_log["Username"].values:
        raise HTTPException(status_code=400, detail="Seller not found")
    seller_password = seller_log.loc[
        seller_log["Username"] == seller.username, "Password"
    ].values[0]
    if seller.password != seller_password:
        raise HTTPException(status_code=400, detail="Wrong password")
    else:
        with open(r"data\ulogovani_prodavci.json", "r") as f:
            seler_json = json.load(f)
            for logged_seller in seler_json:
                if logged_seller["username"] == seller.username:
                    raise HTTPException(
                        status_code=400, detail="Prodavac je već ulogovan"
                    )
        seller_json = {"username": seller.username, "password": seller.password}
        seler_json.append(seller_json)
        with open(r"data\ulogovani_prodavci.json", "w") as f:
            json.dump(seler_json, f, indent=6)
        return {"message": "Login successful"}

