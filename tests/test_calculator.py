import unittest
from calculator import add, subtract, multiply, divide, power

class TestCalculatorOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-3, 3), -9)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(4, 0.5), 2)

if __name__ == '__main__':
    unittest.main()
