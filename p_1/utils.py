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
        return False


def add_product(naziv, kolicina):
    with open(r"data/proizvod.json", "r") as f:
        store = json.load(f)
        for x in store:
            if x["name"] == naziv and x["quantity"] >= int(kolicina):
                y = {
                    "name": x["name"],
                    "price": x["price"],
                    "quantity": int(kolicina),
                }
                with open(r"data/korpa.json", "r") as f:
                    korpa = json.load(f)
                for proizvod in korpa:
                    if proizvod["name"] == naziv:
                        proizvod["quantity"] += int(kolicina)
                        break
                else:
                    korpa.append(y)
                out_file = open(r"data/korpa.json", "w")
                json.dump(korpa, out_file, indent=6)
                return True
        else:
            print("\npogresan izbor\n")
            return False


def view_store():
    with open(r"data/proizvod.json", "r") as f:
        store = json.load(f)
        print(store)


def change_store(naziv, kolicina):
    with open(r"data/proizvod.json", "r") as f:
        store = json.load(f)
        for product in store:
            if naziv == product["name"]:
                product["quantity"] = product["quantity"] - int(kolicina)
    with open(r"data/proizvod.json", "w") as f:
        json.dump(store, f, indent=6)


def change_korpa(naziv_k, kolicina_k):
    with open(r"data/korpa.json", "r") as f:
        korpa = json.load(f)
        for product in korpa:
            if naziv_k != product["name"] or int(kolicina_k) > product["quantity"]: 
                print("\npogresan izbor\n") 
                return None
    with open(r"data/korpa.json", "r") as f:
        korpa = json.load(f)
        for product in korpa:
            if naziv_k == product["name"] and int(kolicina_k) < product["quantity"]:
                product["quantity"] = product["quantity"]-int(kolicina_k)
                with open(r"data/proizvod.json", "r") as f:
                    store = json.load(f)
                    for product in store:
                        if naziv_k == product["name"]:
                            product["quantity"]+=int(kolicina_k)

                            with open(r"data/korpa.json", "w") as f:
                                json.dump(korpa, f, indent=6)
                            with open(r"data/proizvod.json", "w") as f:
                                json.dump(store, f, indent=6)
                                break
        else:
            with open(r"data/korpa.json", "r") as f:
                korpa = json.load(f)
                z =[]
                for product in korpa:
                    if naziv_k == product["name"] and product["quantity"] == int(kolicina_k):
                        pass
                   
                    else:
                        z.append(product)
                        break          

                with open(r"data/proizvod.json", "r") as f:
                    store = json.load(f)
                    for product in store:
                        if naziv_k == product["name"]:
                            product["quantity"]+=int(kolicina_k)

                        with open(r"data/korpa.json", "w") as f:
                            json.dump(z, f, indent=6)
                        with open(r"data/proizvod.json", "w") as f:
                            json.dump(store, f,indent=6)  
                              
    
                
                          
            
                
                
                


    
        