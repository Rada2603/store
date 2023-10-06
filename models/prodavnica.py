import json


class Store:
    def view_store():
        with open(r"data/proizvod.json", "r") as f:
            store = json.load(f)
            print(store)

    def change_store(naziv, kolicina):
        new_product = []
        with open(r"data/proizvod.json", "r") as f:
            store = json.load(f)

            for product in store:
                if naziv == product["name"]:
                    name = product["name"]
                    price = product["price"]
                    quantity = product["quantity"] - int(kolicina)

                    new_product.append(
                        {"name": name, "price": price, "quantity": quantity}
                    )

                else:
                    new_product.append(product)
        with open(r"data/proizvod.json", "w") as f:
            json.dump(new_product, f)
