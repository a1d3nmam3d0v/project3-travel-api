import requests
import os
import json
import logging
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


def send_latest_exchange_rate_request(headers,query):


    try:
        response = requests.get(url, params=query, headers=headers)

        # print(response.status_code)
        if response.raise_for_status== 404: # currency not found or doesnt exist 
              return None, 'Currency rate not found'
        response.raise_for_status() 
        response_data =response.json()
        return response_data

    except Exception as e:
        logging.exception(e)
        return None, 'Error connecting to currency website '

        
            
       

def build_query_string (home_currency, foreign_currency):
    #create a dictionary of query parameters for the API
    query = {'from': home_currency, 'to': foreign_currency, 'amount': 1}

    return query

def build_request_headers():
    # generate headers used in the API requests 
    headers = {'apikey': key}
    return headers



"""This function is to return a list of from currency , to currency and the exchange rate"""

def extract_latest_rate_data(api_response):

    from_currency = api_response['query']['from']
    to_currency = api_response['query']['to']
    rate = api_response['info']['rate']

    exchange_rate_data = [from_currency, to_currency, rate]
    return exchange_rate_data


if __name__ =='__main__':
        print()