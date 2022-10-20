

from msilib.schema import Error
import requests
import os
import json
from pprint import pprint






class API_Response:
    def __init__(self,data,user_error,server_error):
        self.data=data
        self.user_error=user_error
        self.server_error=server_error

    def is_sucess(self):
        return self.data and not self.user_error and not self.server_error



url='https://api.apilayer.com/fixer/latest?symbols={symbols}&base={base}'
key=os.environ.get('apiKey')

def get_exchange_rate(home_currency,foreign_currency):
    
  
        query_parameters=build_query_string(home_currency, foreign_currency)
        api_response=send_latest_exchange_rate(url,query_parameters)

        return api_response



def send_latest_exchange_rate(url,query_parameters):

    try:
        response = requests.get(url,query_parameters)
        response.raise_for_status() # raise exception for 400 or 500 errors
        response_data =response.json()
        data=extract_latest_rate_data()
        return API_Response(data,None,None)

    except Exception as e:

        if Error:
            api_error_message = ('202, 201')

            return API_Response(None, api_error_message, None)

        else:
            return API_Response(None,None, e) 
            
       
        





def build_query_string (home_currency,foreign_currency ):

    #create a dictionary of query parameters for the API

    {
    home_currency:'EUR',
    foreign_currency:('JPY','GBP','USD','INR')

    }


def extract_latest_rate_data(api_response):
  #Read from the json and return it 
  {
  'timestamp': api_response.get('timestamp'),
  'date': api_response.get('date'),
  'rates': api_response.get('rates'),

  }

if __name__ =='__main__':

        response =get_exchange_rate('GBP','USD')
        print(response.data,response.user_error,response.server_error)

        get_exchange_rate('23678', 'USD')
        print (response.data, response.user_error, response.server_error)
