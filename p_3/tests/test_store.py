import unittest
import pandas as pd
import os
from models.store import Store


class StoreTest(unittest.TestCase):
    def setUp(self) -> None:
        data = {
            "Naziv": ["Kruska", "Jabuka", "Malina"],
            "Cena": [200, 100, 150],
            "Kolicina": [50, 20, 50],
        }
        store_pd = pd.DataFrame(data)
        store_pd.to_csv(r"data_tests\test_store.csv", index=False)

        data = {
            "Naziv": ["Kruska", "Jabuka", "Malina"],
            "Cena": [200, 100, 150],
            "Kolicina": [50, 10, 30],
        }
        korpa_pd = pd.DataFrame(data)
        korpa_pd.to_csv(r"data_tests\test_cart.csv", index=False)
        return super().setUp()

    def tearDown(self) -> None:
        test_store_path = r"data_tests\test_store.csv"
        if os.path.exists(test_store_path):
            os.remove(test_store_path)
        test_cart_path =r"data_tests\test_cart.csv"
        if os.path.exists(test_cart_path):
            os.remove(test_cart_path)
        return super().setUp()

    def test_change_valid_product(self):
        store = Store(
            path_to_store=r"data_tests\test_store.csv",
            path_to_cart=r"data_tests\test_cart.csv",
        )
        self.assertTrue(
            store.check_product_to_store(naziv="Kruska", kolicina=10),
            True,
        )
        prodavnica = pd.read_csv(r"data_tests\test_store.csv")
        self.assertIn("Kruska", prodavnica["Naziv"].values)
        self.assertEqual(
            prodavnica.loc[prodavnica["Naziv"] == "Kruska", "Cena"].values[0], 200
        )
        self.assertEqual(
            prodavnica.loc[prodavnica["Naziv"] == "Kruska", "Kolicina"].values[0], 40
        )

    def test_change_invalid_quantity(self):
        store = Store(
            path_to_store=r"data_tests\test_store.csv",
            path_to_cart=r"data_tests\test_cart.csv",
        )
        self.assertFalse(
            store.check_product_to_store(naziv="Kruska", kolicina=100),
            True,
        )
    
    def test_change_invalid_product(self):
        store = Store(
            path_to_store=r"data_tests\test_store.csv",
            path_to_cart=r"data_tests\test_cart.csv",
        )
        self.assertFalse(
            store.check_product_to_store(naziv="Kokos", kolicina=100),
            True,
        )

    def test_change_valid_product_in_store(self):
        store = Store(
            path_to_store=r"data_tests\test_store.csv",
            path_to_cart=r"data_tests\test_cart.csv",
        )
        self.assertTrue(
            store.change_store(naziv="Kruska", kolicina=10),
            True,
        )
        prodavnica = pd.read_csv(r"data_tests\test_store.csv")
        self.assertIn("Kruska", prodavnica["Naziv"].values)
        self.assertEqual(
            prodavnica.loc[prodavnica["Naziv"] == "Kruska", "Cena"].values[0], 200
        )
        self.assertEqual(
            prodavnica.loc[prodavnica["Naziv"] == "Kruska", "Kolicina"].values[0], 60
        )

    def test_change_invalid_quantity_in_store(self):
        store = Store(
            path_to_store=r"data_tests\test_store.csv",
            path_to_cart=r"data_tests\test_cart.csv",
        )
        self.assertFalse(
            store.change_store(naziv="Kruska", kolicina=100),
            True,
        )

    def test_change_invalid_product_in_store(self):
        store = Store(
            path_to_store=r"data_tests\test_store.csv",
            path_to_cart=r"data_tests\test_cart.csv",
        )
        self.assertFalse(
            store.change_store(naziv="Kokos", kolicina=100),
            True,
        )

if __name__ == "__main__":
    unittest.main()