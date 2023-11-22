from utils_3 import check_option

from models.cart import Cart
from models.store import Store


def main():
    store = Store(r"data\prodavnica.csv", r"data/korpa.csv" )
    cart = Cart(r"data\prodavnica.csv" , r"data/korpa.csv")
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
            store.view_data()
        if opcija == "2":
            naziv = input("Unesi naziv proizvoda :")
            kolicina = input("Unesi kolicinu :")
            store_cena = store.check_product_to_store(naziv, kolicina)
            if not store_cena:
                break
            cart.add_product(naziv, kolicina, store_cena)
        if opcija == "3":
            cart.view_data(store=False)
        if opcija == "4":
            naziv = input("Unesi naziv proizvoda :")
            kolicina = input("Unesi kolicinu :")
            if not store.change_store(naziv, kolicina):
                break
            cart.change_cart(naziv, kolicina)
        if opcija == "5":
            print("IZLAZ")
            break


if __name__ == "__main__":
    main()
