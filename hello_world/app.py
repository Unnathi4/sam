import json

# import requests


def lambda_handler(event, context):
    number1 = event['Number1']
    number2 = event['Number2']
    print(sum(number1,number2))
    print(product(number1,number2))
    print(difference(number1,number2))
    print(quotient(number1,number2))
    
def sum(number1,number2):
   return number1 + number2
def product():
    return number1 * number2
def difference():
    return abs(number1 - number2)
def quotient():
    return number1 / number2
    

