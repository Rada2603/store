from models.view import View
import pandas as pd


class Store(View):
    def __init__(self, path_to_file, path_to_cart=None):
        super().__init__(path_to_file)
        self.path_to_cart = path_to_cart

    def view_store(self):
        df = pd.read_csv(self.path_to_file)
        print(df)

    def change_cart(self, naziv, kolicina) -> bool:
        # Učitaj podatke iz CSV datoteka prodavnice i korpe
        df_prodavnica = pd.read_csv(self.path_to_file)
        df_korpa = pd.read_csv(self.path_to_cart)

        # Proveri da li proizvod postoji u korpi
        if naziv in df_korpa["Naziv"].values:
            cart_kolicina = df_korpa.loc[df_korpa["Naziv"] == naziv, "Kolicina"].values[
                0
            ]

            # Proveri da li željena količina za promenu manja ili jednaka količini u korpi
            if int(kolicina) >= 0 and int(kolicina) <= cart_kolicina:
                # Smanji količinu u korpi
                df_korpa.loc[df_korpa["Naziv"] == naziv, "Kolicina"] -= int(kolicina)

                # Ako je nova količina u korpi nula, ukloni proizvod iz korpe
                if df_korpa.loc[df_korpa["Naziv"] == naziv, "Kolicina"].values[0] == 0:
                    df_korpa = df_korpa[df_korpa["Naziv"] != naziv]

                # Ažuriraj količinu u prodavnici
                df_prodavnica.loc[df_prodavnica["Naziv"] == naziv, "Kolicina"] += int(
                    kolicina
                )

                # Sačuvaj ažurirane CSV datoteke
                df_korpa.to_csv(self.path_to_cart, index=False)
                df_prodavnica.to_csv(self.path_to_file, index=False)
                return True

            else:
                print("\nPogresna kolicina\n")
                return False
        else:
            print("\nPogresan Proizvod\n")
            return False
