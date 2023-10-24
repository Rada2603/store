from fastapi import FastAPI
from models.store import (
    view_store,
    add_new_product_in_store,
    change_quantity_product_in_store,
)
from models.cart import (
    view_cart_stefan,
    add_product_stefancart,
    delete_product_cart,
    view_cart_olivera,
)
from models.login import login_seller, login_customer
import uvicorn
from utils import User, Product


app = FastAPI()


@app.get("/store")
def view_store_route():
    return view_store()


@app.get("/stefan")
def view_cart_stefan_route():
    return view_cart_stefan()


@app.get("/olivera")
def view_cart_olivera_route():
    return view_cart_olivera()


@app.post("/add_product_stef")
def add_product_steafncart_route(kupac: User, product: Product):
    return add_product_stefancart(kupac,product)


@app.post("/change_cart")
def delete_product_cart_route(product: Product):
    return delete_product_cart(product)


@app.post("/logins/")
def login_seller_route(seller: User):
    return login_seller(seller)


@app.post("/add_product_in_store")
def add_new_product_in_store_route(seller: User, product: Product):
    return add_new_product_in_store(seller, product)


@app.post("/change_quantity")
def change_quantity_product_in_store_route(seller: User, product: Product):
    return change_quantity_product_in_store(seller, product)


@app.post("/loginc/")
def login_customer_router(customer: User):
    return login_customer(customer)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
