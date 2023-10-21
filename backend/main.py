import pandas as pd
from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel
import uvicorn

app = FastAPI()


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
def add_cart(naziv: str, kolicina: int):
    korpa = pd.read_csv(r"data\korpa.csv")
    prodavnica = pd.read_csv(r"data\prodavnica.csv")
    if naziv in prodavnica["Naziv"].values:
        if (
            int(kolicina)
            <= prodavnica.loc[prodavnica["Naziv"] == naziv, "Kolicina"].values[0]
        ):
            prodavnica.loc[prodavnica["Naziv"] == naziv, "Kolicina"] -= int(kolicina)
            prodavnica.to_csv(r"data\prodavnica.csv", index=False)
        else:
            raise HTTPException(status_code=400, detail="Pogrešan kolicina")
        if naziv in korpa["Naziv"].values:
            korpa.loc[korpa["Naziv"] == naziv, "Kolicina"] += int(kolicina)
            korpa.to_csv(r"data\korpa.csv", index=False)
        else:
            prodavnica = pd.read_csv(r"data\prodavnica.csv")
            store_cena = prodavnica.loc[prodavnica["Naziv"] == naziv, "Cena"].values[0]
            novi_proizvod = {
                "Naziv": naziv,
                "Cena": store_cena,
                "Kolicina": kolicina,
            }
            korpa = korpa._append(novi_proizvod, ignore_index=True)
            korpa.to_csv(r"data\korpa.csv", index=False)
    else:
        raise HTTPException(status_code=400, detail="Pogrešan proizvod")
    return korpa.to_dict(orient="records"), prodavnica.to_dict(orient="records")


@app.post("/change_cart")
def delete_product_cart(naziv: str, kolicina: int):
    korpa = pd.read_csv(r"data\korpa.csv")
    prodavnica = pd.read_csv(r"data\prodavnica.csv")
    if naziv in korpa["Naziv"].values:
        cart_kolicina = korpa.loc[korpa["Naziv"] == naziv, "Kolicina"].values[0]
        if int(kolicina) < cart_kolicina:
            prodavnica.loc[prodavnica["Naziv"] == naziv, "Kolicina"] += int(kolicina)
            korpa.loc[korpa["Naziv"] == naziv, "Kolicina"] -= int(kolicina)
            prodavnica.to_csv(r"data\prodavnica.csv", index=False)
            korpa.to_csv(r"data\korpa.csv", index=False)
        elif int(kolicina) == cart_kolicina:
            prodavnica.loc[prodavnica["Naziv"] == naziv, "Kolicina"] += int(kolicina)
            korpa = korpa[korpa["Naziv"] != naziv]
            prodavnica.to_csv(r"data\prodavnica.csv", index=False)
            korpa.to_csv(r"data\korpa.csv", index=False)
        else:
            raise HTTPException(status_code=400, detail="Pogrešan kolicina")
    else:
        raise HTTPException(status_code=400, detail="Pogrešan proizvod")
    return korpa.to_dict(orient="records"), prodavnica.to_dict(orient="records")


class TestData(BaseModel):
    naziv: str
    kolicina: int


@app.post("/test")
def test(data: TestData):

    print(data.naziv)
    print(data.kolicina)

    return data.dict()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
