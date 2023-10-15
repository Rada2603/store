import pandas as pd


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


def change_cart(
    naziv,
    kolicina,
    path_store: str = r"data\prodavnica.csv",
    path_cart: str = r"data\korpa.csv",
) -> bool:
    df_prodavnica = pd.read_csv(path_store)
    df_korpa = pd.read_csv(path_cart)
    if naziv in df_korpa["Naziv"].values:
        cart_kolicina = df_korpa.loc[df_korpa["Naziv"] == naziv, "Kolicina"].values[0]
        if cart_kolicina > int(kolicina):
            df_korpa.loc[df_korpa["Naziv"] == naziv, "Kolicina"] -= int(kolicina)
            df_prodavnica.loc[df_prodavnica["Naziv"] == naziv, "Kolicina"] += int(
                kolicina
            )
            df_korpa.to_csv(path_cart, index=False)
            df_prodavnica.to_csv(path_store, index=False)
            return True
        elif cart_kolicina == int(kolicina):
            df_korpa = df_korpa[df_korpa["Naziv"] != naziv]
            df_korpa.to_csv(path_cart, index=False)
            df_prodavnica.loc[df_prodavnica["Naziv"] == naziv, "Kolicina"] += int(
                kolicina
            )
            df_prodavnica.to_csv(path_store, index=False)
            return True
        else:
            print("\nPogresna kolicina\n")
            return False
    else:
        print("\nPogresan Proizvod\n")
        return False
