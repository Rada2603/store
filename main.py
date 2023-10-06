import json
from utils import check_option
from models.prodavnica import Store
from models.korpa import Cart


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
            Store.view_store()
        if opcija == "2":
            naziv, kolicina = Cart.check_korpa()
            Cart.add_product(naziv, kolicina)
            Store.change_store(naziv, kolicina)
            
        if opcija == "3":
            with open(r"data/korpa.json", "r") as f:
                korpa_k = json.load(f)
                print(korpa_k)

        if opcija == "4":
            new_corpa = []
            with open(r"data/korpa.json", "w") as f:
                korpa_h = json.dump(new_corpa, f)
                print(korpa_h)
        if opcija == "5":
            print("izlaz")
            break


if __name__ == "__main__":
    main()
