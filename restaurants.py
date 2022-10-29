import re
from urllib import response
import requests
import os

url = 'https://api.yelp.com/v3/businesses/search'
token = os.environ.get('yelp_token')
headers = {'Authorization' : token}

def get_restaurants(city, country, result_limit):
    city = clean_up_input(city)
    country = clean_up_input(country)

    try:
        query = {'term': 'restaurants', 'location': f'{city}+{country}', 'sort_by': 'rating', 'limit': result_limit}
        response = requests.get(url, params=query, headers=headers)
        response.raise_for_status()
        data = response.json()
        data = data['businesses']
        return data
    except Exception as ex:
        print(ex)
        print(response.text)
        return None

def filter_restaurants(city, country, restaurant_data):
    city = clean_up_input(city)
    country = clean_up_input(country)
    restaurant_list = []

    for restaurant in restaurant_data:
        if restaurant['location']['city'].lower() == city and restaurant['location']['country'].lower() == country:
            restaurant_list.append(restaurant)
            if len(restaurant_list) == 3:
                break

    return restaurant_list

def clean_up_input(text):
    return text.strip().lower()
