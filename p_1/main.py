import json
from utils import check_option, add_product, change_store, view_store, change_korpa


def main():
    print("Dobro dosli")
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
            view_store()
        if opcija == "2":
            naziv = input("Unesi ime proizvoda :")
            kolicina = input("Unesi kolicinu :")
            if add_product(naziv, kolicina):
                change_store(naziv, kolicina)
        if opcija == "3":
            # TODO: First return products to the product list, then empty the cart
            with open(r"data/korpa.json", "r") as f:
                korpa_k = json.load(f)
                print(korpa_k)
        if opcija == "4":
            naziv_k = input("Unesi naziv proizvoda koji zelis da obrises :")
            kolicina_k = input("Unesi kolicinu")
            change_korpa(naziv_k, kolicina_k)

        if opcija == "5":
            print("izlaz")
            break


if __name__ == "__main__":
    main()
