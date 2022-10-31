import requests
import os
import json
from pprint import pprint


url='https://api.apilayer.com/fixer/convert'
key=os.environ.get('CURRENCY_API_KEY')


def get_exchange_rate(home_currency,foreign_currency):
    
    query_parameters=build_query_string(home_currency, foreign_currency)
    api_response=send_latest_exchange_rate(url,query_parameters)

    return api_response


def send_latest_exchange_rate(headers,query):

    headers = {'apikey': key}

    try:
        response = requests.get(url, params=query, headers=headers)
        response.raise_for_status() # raise exception for 400 or 500 errors
        response_data =response.json()
        data=extract_latest_rate_data()
        return data

    except Exception as e:
        print(e)
        print(response.text)
            
       

def build_query_string (home_currency, foreign_currency):
    #create a dictionary of query parameters for the API
    query = {'from': home_currency, 'to': foreign_currency, 'amount': 1}
    return query


"""This function is to return a list of two elemenets with the exchange rate and the timestamp """

def extract_latest_rate_data(api_response):

    exchange_rate_data = []

    from_currency = api_response['query']['from']
    to_currency = api_response['query']['to']
    rate = api_response['info']['rate']

    exchange_rate_data.append([from_currency, to_currency, rate])

    return exchange_rate_data


if __name__ =='__main__':
        print()