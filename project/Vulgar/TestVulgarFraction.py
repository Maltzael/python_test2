import unittest
from VulgarFraction import VulgarFraction


class TestVukgarFraction(unittest.TestCase):
    def test_add(self):
        a = VulgarFraction(1, 2)
        b = VulgarFraction(1, 2)
        result = a + b
        self.assertEqual(result, VulgarFraction(2, 2))

    def test_add2(self):
        a = VulgarFraction(1, 2)
        b = VulgarFraction(1, 2)
        result = a + b
        self.assertEqual(result, 1)

    def test_sub(self):
        a = VulgarFraction(1, 2)
        b = VulgarFraction(1, 3)
        result = a - b
        self.assertEqual(result, VulgarFraction(1, 6))

    def test_sub2(self):
        a = VulgarFraction(1, 2)
        b = 2
        result = a - b
        self.assertEqual(result, -1.5)

    def test_mul(self):
        a = VulgarFraction(2, 1)
        b = VulgarFraction(1, 2)
        result = a * b
        self.assertEqual(result, VulgarFraction(1, 1))

    def test_mul2(self):
        a = VulgarFraction(2, 1)
        b = 1.5
        result = a * b
        self.assertEqual(result, 3)

    def test_truediv(self):
        a = VulgarFraction(22, 1)
        b = VulgarFraction(22, 1)
        result = a / b
        self.assertEqual(result, VulgarFraction(1, 1))

    def test_truediv2(self):
        a = VulgarFraction(40, 2)
        b = 0.1
        result = a / b
        self.assertEqual(result, 200)

    def test_eq(self):
        a = VulgarFraction(22, 1)
        b = VulgarFraction(22, 1)
        result = a == b
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
