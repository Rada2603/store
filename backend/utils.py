from pydantic import BaseModel


class Seller(BaseModel):
    username: str
    password: str


class Product(BaseModel):
    naziv: str
    cena: int
    kolicina: int
