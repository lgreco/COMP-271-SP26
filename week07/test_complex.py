import unittest  # Authorized import for unit testing

# Client specs: give me class Complex in file complex.py
from complex import Complex


class TestComplex(unittest.TestCase):

    # Simple text for addition
    def test_add_positive(self):
        z1 = Complex(3, 4)
        z2 = Complex(1, 2)
        result = z1 + z2
        self.assertEqual(result, Complex(4, 6))

if __name__ == "__main__":
    unittest.main()
