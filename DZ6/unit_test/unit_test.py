#coding=utf-8
import unittest
from DZ63 import factorial

class Testfactorial(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp")
    def test_factorial(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(0), 1)
        self.assertRaises(ValueError, factorial, -1, 2)
        self.assertRaises(ValueError, factorial, 1024, 2)
        self.assertEqual(factorial(3), 6)
    def tearDown(self) -> None:
        print("tearDown")