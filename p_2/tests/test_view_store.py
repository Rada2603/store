import unittest
from unittest.mock import patch, mock_open
from utils_2 import view_store
from io import StringIO
import json


class TestViewStore(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    @patch("json.load", autospec=True)
    def test_view_store(self, mock_json_load, mock_stdout):
        # Postavite očekivane vrednosti koje će se vratiti iz JSON fajla
        expected_data = '{"proizvod1": {"price": 100, "quantity": 50},"proizvod2": {"price": 80, "quantity": 30}}'
        mock_json_load.return_value = expected_data

        # Kreirajte StringIO objekat kako biste uhvatili ispis na standardni izlaz
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            view_store()

        # Proverite da li je ispravno prikazao podatke na standardnom izlazu
        expected_output = """{"proizvod1": {"price": 100, "quantity": 50},
                               "proizvod2": {"price": 80, "quantity": 30}}"""
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main":
    unittest.main()
