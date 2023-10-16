from models.view import View
import pandas as pd


class Cart(View):
    def __init__(self, path_to_store, path_to_cart):
        super().__init__(path_to_store, path_to_cart)

    def check_product(self, naziv, kolicina) -> bool:
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

                Cart.add_product(self,naziv, kolicina,store_cena)
            else:
                print("\nPogresna kolicina\n")
                return False
        else:
            print("\nPogrešan proizvod. Proizvod nije dostupan u prodavnici.\n")
            return False

    def add_product(self, naziv, kolicina, store_cena):
        df_korpa = pd.read_csv(self.path_to_cart)
        if naziv in df_korpa["Naziv"].values:
            df_korpa.loc[df_korpa["Naziv"] == naziv, "Kolicina"] += int(kolicina)
            df_korpa.to_csv(self.path_to_cart, index=False)
            return True
        else:
            novi_proizvod = {
                "Naziv": naziv,
                "Cena": store_cena,
                "Kolicina": kolicina,
            }
            df_korpa = df_korpa._append(novi_proizvod, ignore_index=True)
            df_korpa.to_csv(self.path_to_cart, index=False)
        return True
