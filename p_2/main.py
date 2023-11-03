from utils_2 import check_option, view_store, add_cart, view_cart, change_cart


def main():
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
            view_store()
        if opcija == "2":
            naziv = input("Unesi naziv proizvoda :")
            kolicina = input("Unesi kolicinu :")
            add_cart(naziv, kolicina)
        if opcija == "3":
            view_cart()
        if opcija == "4":
            naziv = input("Unesi naziv proizvoda :")
            kolicina = input("Unesi kolicinu :")
            change_cart(naziv, kolicina)
        if opcija == "5":
            print("\nIZLAZ")
            break


if __name__ == "__main__":
    main()
