from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class Product(BaseModel):
    naziv: str
    cena: int
    kolicina: int
