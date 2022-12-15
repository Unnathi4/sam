import json

import unittest

import app

class TestSum(unittest.TestCase):

    def test_add(self):
        self.assertEqual(app.sum(2,2), 4)
    def test_product(self):
        self.assertEqual(app.product(3, 2), 6)
    def test_sub(self):
        self.assertEqual(app.difference(4, 1), 3)
    def test_division(self):
        self.assertEqual(app.quotient(4,2), 2)

if __name__ == '__main__':
    unittest.main()

