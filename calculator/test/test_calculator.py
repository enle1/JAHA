import unittest
from calculator import ComplexCalculator

class TestComplexCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(ComplexCalculator.add(complex(1, 2), complex(2, 3)), complex(3, 5))

    def test_magnitude(self):
        self.assertEqual(ComplexCalculator.magnitude(complex(3, 4)), 5.0)

    def test_argument(self):
        self.assertAlmostEqual(ComplexCalculator.argument(complex(1, 1)), 0.7853981633974483)  # π/4

if __name__ == '__main__':
    unittest.main()