import json


def check_option(opcija: str) -> bool:
    """
    Check if the option is valid(1  to 5)

    Args: opcija(str): opcija

    Returns:
           bool: True if opcija is valid , False otherwise
    """
    try:
        if int(opcija) < 1 or int(opcija) > 5:
            print("\npogresan izbor\n")
            return False

        else:
            print(f"\nopcija:{opcija}\n")
            return True

    except Exception:
        print("\npogresan izbor\n")


def view_store():
    with open(r"data\prodavnica2.json", "r") as f:
        store = json.load(f)
        print(store)


def add_cart(naziv, kolicina):
    with open(r"data\prodavnica2.json", "r") as f:
        store = json.load(f)
    with open(r"data\korpa2.json", "r") as f:
        korpa = json.load(f)
    if naziv in store:
        if naziv in korpa:
            nova_kolicina = korpa[naziv]["quantity"] + int(kolicina)
        else:
            nova_kolicina = int(kolicina)
        if nova_kolicina <= store[naziv]["quantity"]:
            price = store[naziv]["price"]
            korpa[naziv] = {"price": price, "quantity": nova_kolicina}
            with open(r"data\korpa2.json", "w") as f:
                json.dump(korpa, f, indent=4)
            with open(r"data\prodavnica2.json", "w") as f:
                store[naziv]["quantity"]-= int(kolicina)
                json.dump(store, f, indent=4)
        else:
            print("\nPogresna kolicina\n")
    else:
        print("\nPogresan proizvod\n")


def view_cart():
    with open(r"data\korpa2.json", "r") as f:
        korpa = json.load(f)
        print(korpa)


def change_cart(naziv, kolicina):
    with open(r"data\korpa2.json", "r") as f:
        korpa = json.load(f)
    with open(r"data\prodavnica2.json", "r") as f:
        store = json.load(f)
    if naziv in korpa:
        if int(kolicina) < korpa[naziv]["quantity"]:
            korpa[naziv]["quantity"]-= int(kolicina)
        elif int(kolicina) ==  korpa[naziv]["quantity"]:
            del korpa[naziv]  
            with open(r"data\korpa2.json", "w") as f:
                json.dump(korpa, f, indent=4)
            with open(r"data\prodavnica2.json", "w") as f:
                store[naziv]["quantity"] += int(kolicina)
                json.dump(store, f, indent=4)  
        else:
            print("\nPogresna kolicina")
    else:
        print("\nPogresan proizvod\n")

