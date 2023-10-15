from models.view import View
import pandas as pd


class Cart(View):
    def __init__(self, path_to_file, path_to_store=None):
        super().__init__(path_to_file)
        self.path_to_store = path_to_store

    def view_cart(self):
        df = pd.read_csv(self.path_to_file)
        print(df)

    def add_to_cart(self, naziv, kolicina) -> bool:
        """Ucitaj podatke iz csv"""
        df_prodavnica = pd.read_csv(self.path_to_store)
        df_korpa = pd.read_csv(self.path_to_file)

        """Proveri da li proizvod postoji u prodavnic"""
        if naziv in df_prodavnica["Naziv"].values:
            """Dobij trenutnu količinu u prodavnici"""
            store_kolicina = df_prodavnica.loc[
                df_prodavnica["Naziv"] == naziv, "Kolicina"
            ].values[0]

            """Proveri da li ima dovoljno proizvoda na stanju"""
            if store_kolicina >= int(kolicina):
                """Smanji količinu u prodavnici"""
                df_prodavnica.loc[df_prodavnica["Naziv"] == naziv, "Kolicina"] -= int(
                    kolicina
                )

                """Sačuvaj ažuriranu prodavnicu"""
                df_prodavnica.to_csv(self.path_to_store, index=False)

                """Proveri da li proizvod već postoji u korpi"""
                if naziv in df_korpa["Naziv"].values:
                    """Ako postoji, dodaj količinu"""
                    df_korpa.loc[df_korpa["Naziv"] == naziv, "Kolicina"] += int(
                        kolicina
                    )

                else:
                    """Ako ne postoji, dodaj novi proizvod u korpu"""
                    novi_proizvod = {"Naziv": naziv, "Cena": 150, "Kolicina": kolicina}
                    df_korpa = df_korpa._append(novi_proizvod, ignore_index=True)

                """Sačuvaj ažuriranu korpu"""
                df_korpa.to_csv(self.path_to_file, index=False)
                return True
            else:
                print("\nPogresna kolicina\n")
                return False
        else:
            print("\ngreska\n")
            return False
