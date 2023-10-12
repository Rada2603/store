import unittest
from unittest.mock import patch
from utils_2 import view_store
import json


class TestViewStore(unittest.TestCase):
    @patch('builtins.print')
    def test_view_store(self, mock_print):
        view_store()  
        mock_print.assert_called_with(json.load(open(r"data\prodavnica2.json")))



if __name__ == '__main__':
    unittest.main()

