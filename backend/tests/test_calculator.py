import unittest
from api.core.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(4, Calculator.calculate("2 2 +"))

    def test_subtract(self):
        self.assertEqual(2, Calculator.calculate("4 2 -"))

    def test_multiply(self):
        self.assertEqual(8, Calculator.calculate("2 4 *"))

    def test_divide(self):
        self.assertEqual(2, Calculator.calculate("8 4 /"))

    def test_add_many_numbers(self):
        self.assertEqual(10, Calculator.calculate("1 2 + 3 4 + + "))

    def test_mixed_operations(self):
        self.assertEqual(42, Calculator.calculate("3 4 * 5 6 * + "))

    def test_exponent(self):
        self.assertEqual(4, Calculator.calculate("2 2 ^"))


if __name__ == "__main__":
    unittest.main()
