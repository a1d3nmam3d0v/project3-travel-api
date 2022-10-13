
import requests
import os
from pprint import pprint
import json




 
def currency_conversion():


    headers = {"apikey": os.environ["apiKey"]}

    base=input("Enter From Currency:").upper()
    symbols=input("Enter To currency:").upper()

    response = requests.request("GET", f"https://api.apilayer.com/fixer/latest?symbols={symbols}&base={base}", headers=headers)

    response_json=response.json()

 
    if response_json['success']:

        rate=response.json()['rates'][symbols]

        amount=float(input("Enter the amount:"))

        convertedAmount= amount * rate

        print("{:.2f}".format(convertedAmount))

    else:
        print('Request unsuccessful')


currency_conversion()