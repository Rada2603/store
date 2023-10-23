
from fastapi import FastAPI
from models.store import view_store, change_store
from models.cart import view_cart, add_cart, delete_product_cart
from models.login import login_seller
import uvicorn
from utils import Seller, Product

app = FastAPI()


@app.get("/store")
def view_store_route():
    return view_store()  


@app.get("/cart")
def view_cart_route():
    return view_cart()


@app.post("/add_product")
def add_cart_route(product: Product):
    return add_cart(product)


@app.post("/change_cart")
def delete_product_cart_route(product: Product):
    return delete_product_cart(product)


@app.post("/login/")
def login_seller_route(seller: Seller):
    return login_seller(seller)


@app.post("/change_store")
def change_store_route(seller: Seller, product: Product):
    return change_store(seller, product)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
