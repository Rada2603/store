import unittest
import pandas as pd
import os
from models.cart import Cart


class CartTest(unittest.TestCase):
    def setUp(self) -> None:
        data = {
            "Naziv": ["Kruska", "Jabuka"],
            "Cena": [200, 100],
            "Kolicina": [50, 20],
        }
        cart_pd = pd.DataFrame(data)
        cart_pd.to_csv(r"data_tests\test_cart.csv", index=False)
        return super().setUp()

    def tearDown(self) -> None:
        test_cart_path = r"data_tests\test_cart.csv"
        if os.path.exists(test_cart_path):
            os.remove(test_cart_path)
        return super().setUp()
    
    def test_ad_exist_product(self):
        cart = Cart(
            path_to_store=r"data_tests\test_store.csv",
            path_to_cart=r"data_tests\test_cart.csv",
        )
        self.assertTrue(
            cart.add_product(naziv="Jabuka", kolicina=5, store_cena=100),
            True,
        )
        korpa = pd.read_csv(r"data_tests\test_cart.csv")
        self.assertIn("Jabuka", korpa["Naziv"].values)
        self.assertEqual(korpa.loc[korpa["Naziv"] == "Jabuka", "Cena"].values[0], 100)
        self.assertEqual(
            korpa.loc[korpa["Naziv"] == "Jabuka", "Kolicina"].values[0], 25
        )
       
    def test_ad_new_product(self):
        cart = Cart(
            path_to_store=r"data_tests\test_store.csv",
            path_to_cart=r"data_tests\test_cart.csv",
        )
        self.assertTrue(
            cart.add_product(naziv="Malina", kolicina=5, store_cena=120)
            True,
        )
        korpa = pd.read_csv(r"data_tests\test_cart.csv")
        self.assertIn("Malina", korpa["Naziv"].values)
        self.assertEqual(korpa.loc[korpa["Naziv"] == "Malina", "Cena"].values[0], 120)
        self.assertEqual(korpa.loc[korpa["Naziv"] == "Malina", "Kolicina"].values[0], 5)
        
    def test_change_cart(self):
        cart = Cart(
            path_to_store=r"data_tests\test_store.csv",
            path_to_cart=r"data_tests\test_cart.csv",
        )
        self.assertTrue(
            cart.change_cart(naziv="Kruska", kolicina=10),
            True,
        )
        korpa = pd.read_csv(r"data_tests\test_cart.csv")
        self.assertIn("Kruska", korpa["Naziv"].values)
        self.assertEqual(korpa.loc[korpa["Naziv"] == "Kruska", "Cena"].values[0], 200)
        self.assertEqual(
            korpa.loc[korpa["Naziv"] == "Kruska", "Kolicina"].values[0], 40
        )
        
    def test_change_1_cart(self):
        cart = Cart(
            path_to_store=r"data_tests\test_store.csv",
            path_to_cart=r"data_tests\test_cart.csv",
        )
        self.assertTrue(
            cart.change_cart(naziv="Kruska", kolicina=50),
            True,
        )
        korpa = pd.read_csv(r"data_tests\test_cart.csv")
        self.assertNotIn("Kruska", korpa["Naziv"].values)

    def test_change_2_cart(self):
        cart = Cart(
            path_to_store=r"data_tests\test_store.csv",
            path_to_cart=r"data_tests\test_cart.csv",
        )
        self.assertFalse(
            cart.change_cart(naziv="Kruska", kolicina=100),
            True,
        )


if __name__ == "__main__":
    unittest.main()
