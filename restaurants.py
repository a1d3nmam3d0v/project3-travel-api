from urllib import response
import requests
import os

url = 'https://api.yelp.com/v3/businesses/search'
token = os.environ.get('yelp_token')
headers = {'Authorization' : token}

def get_restaurants(city, country):
    try:
        query = {'term': 'restaurants', 'location': f'{city} {country}', 'sort_by': 'rating', 'limit': 3}
        response = requests.get(url, params=query, headers=headers)
        response.raise_for_status()
        data = response.json()
        data = data['businesses']
        return data
    except Exception as ex:
        print(ex)
        print(response.text)
        return None







   


