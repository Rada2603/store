from models.view import View
import pandas as pd


class Store(View):
    def __init__(self, path_to_store, path_to_cart):
        super().__init__(path_to_store, path_to_cart)

    def check_product_to_store(self, naziv, kolicina) -> bool:
        df_prodavnica = pd.read_csv(self.path_to_store)
        if naziv in df_prodavnica["Naziv"].values:
            if (
                int(kolicina)
                <= df_prodavnica.loc[
                    df_prodavnica["Naziv"] == naziv, "Kolicina"
                ].values[0]
            ):
                df_prodavnica.loc[df_prodavnica["Naziv"] == naziv, "Kolicina"] -= int(
                    kolicina
                )

                df_prodavnica.to_csv(self.path_to_store, index=False)
                store_cena = df_prodavnica.loc[
                    df_prodavnica["Naziv"] == naziv, "Cena"
                ].values[0]
                print("11111")
                return store_cena
            else:
                print("\nPogresna kolicina\n")
                return False
        else:
            print("\nPogrešan proizvod. Proizvod nije dostupan u prodavnici.\n")
            return False

    def change_store(self, naziv, kolicina) -> bool:
        df_prodavnica = pd.read_csv(self.path_to_store)
        df_korpa = pd.read_csv(self.path_to_cart)
        if naziv in df_korpa["Naziv"].values:
            cart_kolicina = df_korpa.loc[df_korpa["Naziv"] == naziv, "Kolicina"].values[
                0
            ]
            if int(kolicina) <= cart_kolicina:
                df_prodavnica.loc[df_prodavnica["Naziv"] == naziv, "Kolicina"] += int(
                    kolicina
                )
                df_prodavnica.to_csv(self.path_to_store, index=False)
                print("22222222")
                return True
            else:
                print("\nPogresna kolicina")
        else:
            print("\nPogresan Proizvod\n")
            return False
