import unittest
from do_prime_factorization import do_prime_factorization

class TestDoPrimeFactorization(unittest.TestCase):
    def test_do_prime_factorization(self) -> None:
        self.assertEqual(do_prime_factorization(1), {1: 1})
        self.assertEqual(do_prime_factorization(3), {3: 1})
        self.assertEqual(do_prime_factorization(6), {2: 1, 3: 1})
        self.assertEqual(do_prime_factorization(30), {2: 1, 3: 1, 5: 1})
        self.assertEqual(do_prime_factorization(11), {11: 1})
        self.assertEqual(do_prime_factorization(123456789011
                                                ), {123456789011: 1})
        self.assertEqual(do_prime_factorization(280), {2: 3, 5: 1, 7: 1})


if __name__ == '__main__':
    unittest.main()
