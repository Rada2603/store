from models.view import View
import pandas as pd


class Cart(View):
    def __init__(self, path_to_store, path_to_cart):
        super().__init__(path_to_store, path_to_cart)

    
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
    
    def change_cart(self, naziv, kolicina) ->bool:
        df_korpa = pd.read_csv(self.path_to_cart)
        cart_kolicina = df_korpa.loc[df_korpa["Naziv"]== naziv, "Kolicina"].values[0]
        if int(kolicina) < cart_kolicina:
            print("*******")
            df_korpa.loc[df_korpa["Naziv"]== naziv, "Kolicina"] -= int(kolicina)
            df_korpa.to_csv(self.path_to_cart, index=False)
            print("1111")
            return True
        elif int(kolicina) == cart_kolicina:
            df_korpa = df_korpa[df_korpa["Naziv"] != naziv] 
            df_korpa.to_csv(self.path_to_cart, index=False)
            return True
        else:
            print("\nPogresna kolicina\n")
            return False