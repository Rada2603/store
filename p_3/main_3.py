from utils_3 import check_option
from models.store import Store
from models.cart import Cart


def main():
    prodavnica = Store(r"data\prodavnica.csv", r"data\korpa.csv")
    korpa = Cart(r"data\korpa.csv", r"data\prodavnica.csv")
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
            prodavnica.view_store()
        if opcija == "2":
            naziv = input("Unesi naziv proizvoda :")
            kolicina = input("Unesi kolicinu :")
            korpa.add_to_cart(naziv, kolicina)
        if opcija == "3":
            korpa.view_cart()
        if opcija == "4":
            naziv = input("Unesi naziv proizvoda :")
            kolicina = input("Unesi kolicinu :")
            change_cart(naziv, kolicina)
        if opcija == "5":
            print("IZLAZ")
            break


if __name__ == "__main__":
    main()
