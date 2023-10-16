from utils_3 import check_option
from models.view import View
from models.cart import Cart
from models.store import Store


def main():
    view = View(r"data\prodavnica.csv", r"data/korpa.csv")
    store = Cart(r"data\prodavnica.csv", r"data/korpa.csv" )
    cart = Store(r"data\prodavnica.csv" , r"data/korpa.csv")
    print("\nDobro dosli\n")
    while True:
        print("1.Prikazi proizvode")
        print("2.Dodaj u korpu")
        print("3.Prikazi korpu")
        print("4.Isprazni korpu")
        print("5.Izlaz")
        opcija = input("Izaberi opciju:")
        if not check_option(opcija):
            continue
        if opcija == "1":
            view.view_data()
        if opcija == "2":
            naziv = input("Unesi naziv proizvoda :")
            kolicina = input("Unesi kolicinu :")
            store.check_product(naziv, kolicina)
        if opcija == "3":
            view.view_data(store=False)
        if opcija == "4":
            naziv = input("Unesi naziv proizvoda :")
            kolicina = input("Unesi kolicinu :")
            cart.change_store(naziv, kolicina)
        if opcija == "5":
            print("IZLAZ")
            break


if __name__ == "__main__":
    main()
