import unittest
from euclidAlgo import EuclideanAlgorithm

class TestEuclidAlgo(unittest.TestCase):
    def test_1(self):
        ea = EuclideanAlgorithm()
        res = ea.gcd(27, 21)
        self.assertEqual(res, 3)
    
    def test_2(self):
        ea = EuclideanAlgorithm()
        res = ea.gcd(301, 973)
        self.assertEqual(res, 7)

if __name__ == "__main__":
    unittest.main()