import unittest
from p_2.utils_2 import check_option


class TestCheckOption(unittest.TestCase):
    def test_valid_option1(self):
        result = check_option("1")
        self.assertTrue(result, "Expected a valid option")

    def test_valid_option2(self):
        result = check_option("2")
        self.assertTrue(result, "Expected a valid option")

    def test_valid_option3(self):
        result = check_option("3")
        self.assertTrue(result, "Expected a valid option")  

    def test_valid_option4(self):
        result = check_option("4")
        self.assertTrue(result, "Expected a valid option")

    def test_valid_option5(self):
        result = check_option("5")
        self.assertTrue(result, "Expected a valid option")

    def test_valid_option_low(self):
        result = check_option("0")
        self.assertFalse(result, "Expected a valid option")
    
    def test_invalid_option_high(self):
        result = check_option("6")
        self.assertFalse(result, "Expected an invalid option")

    def test_invalid_option_non_integer(self):
        result = check_option("abc")
        self.assertFalse(result, "Expected an invalid option")

    

if __name__ == "__main__":
    unittest.main()