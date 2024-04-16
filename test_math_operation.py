import unittest
from math_tool import MathTool

class TestMathTool(unittest.TestCase):
    def setUp(self):
        self.math_tool = MathTool()

    def test_add_positive_numbers(self):
        result = self.math_tool.add(3, 4)
        self.assertEqual(result, 7)

    def test_add_negative_numbers(self):
        result = self.math_tool.add(-3, -4)
        self.assertEqual(result, -7)

    def test_add_mixed_numbers(self):
        result = self.math_tool.add(3, -4)
        self.assertEqual(result, -1)

    def test_subtract_positive_numbers(self):
        result = self.math_tool.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_subtract_negative_numbers(self):
        result = self.math_tool.subtract(-5, -2)
        self.assertEqual(result, -3)

    def test_multiply_positive_numbers(self):
        result = self.math_tool.multiply(2, 3, 4)
        self.assertEqual(result, 24)

    def test_multiply_negative_numbers(self):
        result = self.math_tool.multiply(-2, -3, -4)
        self.assertEqual(result, -24)

    def test_divide_positive_numbers(self):
        result = self.math_tool.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.math_tool.divide(10, 0)

    def test_power_positive_numbers(self):
        result = self.math_tool.power(2, 3)
        self.assertEqual(result, 8)

    def test_power_negative_exponent(self):
        result = self.math_tool.power(2, -3)
        self.assertEqual(result, 0.125)

    def test_sqrt_positive_number(self):
        result = self.math_tool.sqrt(16)
        self.assertEqual(result, 4)

    def test_sqrt_negative_number(self):
        with self.assertRaises(ValueError):
            self.math_tool.sqrt(-16)

if __name__ == '__main__':
    unittest.main()
