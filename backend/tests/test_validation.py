import unittest

from api.schemas.calculation import check_expression_length, check_symbols_presence


class ValidationTestCase(unittest.TestCase):
    def test_check_symbols_presence(self):
        self.assertEqual("2 2 + 3 4 + *", check_symbols_presence("2 2 + 3 4 + *"))

    def test_check_symbols_absence(self):
        with self.assertRaises(ValueError):
            check_symbols_presence("2 2 ")

    def test_check_symbols_no_digits(self):
        with self.assertRaises(ValueError):
            check_symbols_presence("+ + +")

    def test_check_expression_length(self):
        self.assertEqual("2 2 +", check_expression_length("2 2 +"))

    def test_check_expression_short(self):
        with self.assertRaises(ValueError):
            check_expression_length("2")
