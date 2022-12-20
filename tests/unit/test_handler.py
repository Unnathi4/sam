import json

import unittest

def lambda_handler(event, context):
    number1 = event['Number1']
    number2 = event['Number2']
    print(sum(number1,number2))
    print(product(number1,number2))
    print(difference(number1,number2))
    print(quotient(number1,number2))
    
def sum(number1,number2):
   return number1 + number2
def product(number1,number2):
    return number1 * number2
def difference(number1,number2):
    return abs(number1 - number2)
def quotient(number1,number2):
    return number1 / number2

#Calci class
    
class TestSum(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sum(2,2), 4)
    def test_product(self):
        self.assertEqual(product(4, 2), 8)
    def test_sub(self):
        self.assertEqual(difference(2, 1), 1)
    def test_division(self):
        self.assertEqual(quotient(4,2), 2)

if __name__ == '__main__':
    unittest.main()

