import pandas as pd


class View:
    def __init__(self, path_to_store, path_to_cart):
        self.path_to_store = path_to_store
        self.path_to_cart = path_to_cart

    def view_data(self, store=True):
        if store:
            df = pd.read_csv(self.path_to_store)
        else:
            df = pd.read_csv(self.path_to_cart)
        print(df)
