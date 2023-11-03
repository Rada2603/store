import unittest
from utils_2 import add_cart
import os
import json


class TestAddCart(unittest.TestCase):
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

    def test_add_cart_invalid_product(self):
        self.assertNotEqual(
            add_cart(
                naziv="nepoznat",
                kolicina=3,
                path_store=r"tests\test_data\prodavnica2.json",
                path_korpa=r"tests\test_data\korpa2.json",
            ),
            True,
        )

    def test_add_cart_invalid_quantity(self):
        self.assertNotEqual(
            add_cart(
                naziv="Jabuka",
                kolicina=500,
                path_store=r"tests\test_data\prodavnica2.json",
                path_korpa=r"tests\test_data\korpa2.json",
            ),
            True,
        )

    def test_add_cart_valid_product(self):
        self.assertEqual(
            add_cart(
                naziv="Jabuka",
                kolicina=3,
                path_store=r"tests\test_data\prodavnica2.json",
                path_korpa=r"tests\test_data\korpa2.json",
            ),
            True,
        )

        with open(r"tests\test_data\korpa2.json", "r") as f:
            korpa = json.load(f)
            self.assertIn("Jabuka", korpa)
            self.assertEqual(korpa["Jabuka"]["price"], 100)
            self.assertEqual(korpa["Jabuka"]["quantity"], 13)


if __name__ == "__main":
    unittest.main()
