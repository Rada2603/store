import json
from models.prodavnica import Store


class Cart:
    def add_product(naziv, kolicina):
        with open(r"data/proizvod.json", "r") as f:
            store = json.load(f)
            for x in store:
                if x["name"] == naziv and x["quantity"] >= int(kolicina):
                    y = {
                            "name": x["name"],
                            "price": x["price"],
                            "quantity": int(kolicina)}
                    with open(r"data/korpa.json", "r") as f:
                        korpa = json.load(f)
                        korpa.append(y)
                    out_file = open(r"data/korpa.json", "w")
                    json.dump(korpa, out_file, indent=6)
                    print("======")
                    return naziv, kolicina  
            else:
                print("\npogresan izbor\n")
               
    
    def check_korpa():
        naziv = input("Unesi ime proizvoda :")   
        kolicina = input("Unesi kolicinu :")
        new_product = []
        with open(r"data/korpa.json", "r") as f:
            korpa = json.load(f)
            for x in korpa:
                if  naziv == x["name"]:
                    name = x["name"]
                    price = x["price"]
                    quantity = x["quantity"]+int(kolicina)
                    new_product.append({"name": name, "price": price, "quantity": quantity})
                    with open(r"data/korpa.json", "w") as f:
                        json.dump(new_product, f, indent=6)
                        print("++++++")
                    Store.change_store(naziv, kolicina)
                    
                else:
                    print("-----")
                    new_product.append(x)
                with open(r"data/korpa.json", "w") as f:
                    json.dump(new_product, f, indent=6)
                    print("*****")
            return naziv,kolicina