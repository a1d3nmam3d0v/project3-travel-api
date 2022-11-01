import requests
import os
import json
from pprint import pprint


url='https://api.apilayer.com/fixer/convert'
key=os.environ.get('CURRENCY_API_KEY')


def get_exchange_rate(home_currency,foreign_currency):
    
    query_parameters=build_query_string(home_currency, foreign_currency)
    headers = build_request_headers()
    entire_api_response=send_latest_exchange_rate_request(url, headers, query_parameters)
    if entire_api_response:  
        latest_rate = extract_latest_rate_data(entire_api_response)
        return latest_rate
    else: # the entire_api_response is None, something went wrong
        # TODO change this return something that the caller of this function can check 
        # to see if the request works or not before using the data  
        return 'Error making request'  


# we can mock this
def send_latest_exchange_rate_request(headers, query):  # clarify purpose of function

    try:
        response = requests.get(url, params=query, headers=headers)
        print(response.status_code)  # read the documentation but this is probably 400 
        # if the request is for a currency that doesn't exist or the request is malformed in another way
        # if the user has entered a currency that doesn't exist, your app should display an error message
        # to the user (not crash) and ask them to try again
         
        response.raise_for_status() # raise exception for 400 or 500 errors
        response_data = response.json()
        return response_data

    except Exception as e:
        print(e)
        print(response.text)
        # how will the caller know something has gone wrong? 
        # if you don't return anything, the return value will be None 
        # can you work out how to tell the difference between Server/Program Error (no API key, no internet connection, server down) 
        # and User Error (non-existent currency, no currency entered)?
            

def build_query_string (home_currency, foreign_currency):
    #create a dictionary of query parameters for the API
    query = {'from': home_currency, 'to': foreign_currency, 'amount': 1}
    return query


def build_request_headers():
    # generate headers used in the API requests 
    headers = {'apikey': key}
    return headers


"""This function is to return a list of two elemenets with the exchange rate and the timestamp 
It actually seems to return a list of three things, the from currency, to currency and the rate 
and it's a list inside a list. """

def extract_latest_rate_data(api_response):

    # exchange_rate_data = []

    from_currency = api_response['query']['from']
    to_currency = api_response['query']['to']
    rate = api_response['info']['rate']

    exchange_rate_data = [from_currency, to_currency, rate]  # easier? 

    return exchange_rate_data


if __name__ =='__main__':
    print()