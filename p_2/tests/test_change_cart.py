import unittest
import json
import os
from utils_2 import change_cart


class ChangeCart(unittest.TestCase):
    def setUp(self) -> None:
        data = {
            "Kruska": {"price": 200, "quantity": 180},
            "Malina": {"price": 300, "quantity": 280},
            "Jabuka": {"price": 100, "quantity": 290},
        }
        with open(r"tests\test_data\prodavnica2.json", "w") as f:
            json.dump(data, f)

        data = {
            "Malina": {"price": 300, "quantity": 20},
            "Jabuka": {"price": 100, "quantity": 10},
            "Kruska": {"price": 200, "quantity": 20},
        }
        with open(r"tests\test_data\korpa2.json", "w") as f:
            json.dump(data, f)
        return super().setUp()

    def tearDown(self) -> None:
        json_file_path = r"tests\test_data\prodavnica2.json"
        if os.path.exists(json_file_path):
            os.remove(json_file_path)
        json_file_path = r"tests\test_data\korpa2.json"
        if os.path.exists(json_file_path):
            os.remove(json_file_path)
        return super().tearDown()

    def test_change_valid_product(self):
        self.assertEqual(
            change_cart(
                naziv="Jabuka",
                kolicina=5,
                path_store=r"tests\test_data\prodavnica2.json",
                path_korpa=r"tests\test_data\korpa2.json",
            ),
            True,
        )

        with open(r"tests\test_data\korpa2.json", "r") as f:
            korpa = json.load(f)
            self.assertIn("Jabuka", korpa)
            self.assertEqual(korpa["Jabuka"]["price"], 100)
            self.assertEqual(korpa["Jabuka"]["quantity"], 5)

    def test_change_product_of_cart(self):
        self.assertEqual(
            change_cart(
                naziv="Jabuka",
                kolicina=10,
                path_store=r"tests\test_data\prodavnica2.json",
                path_korpa=r"tests\test_data\korpa2.json",
            ),
            True,
        )
        with open(r"tests\test_data\korpa2.json", "r") as f:
            korpa = json.load(f)
            self.assertNotIn("Jabuka", korpa)
        
        with open( r"tests\test_data\prodavnica2.json","r") as f:
            prodavnica = json.load(f)
            self.assertIn("Jabuka", prodavnica)
            self.assertEqual(prodavnica["Jabuka"]["price"], 100)
            self.assertEqual(prodavnica["Jabuka"]["quantity"], 300)

    def test_change_invalid_product(self):
        self.assertNotEqual(
            change_cart(
                naziv="Kokos",
                kolicina=3,
                path_store=r"tests\test_data\prodavnica2.json",
                path_korpa=r"tests\test_data\korpa2.json",
            ),
            True,
        )

    def test_change_invalid_quantity(self):
        self.assertNotEqual(
            change_cart(
                naziv="Jabuka",
                kolicina=300,
                path_store=r"tests\test_data\prodavnica2.json",
                path_korpa=r"tests\test_data\korpa2.json",
            ),
            True,
        )
