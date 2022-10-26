from urllib import response
import requests
import os

url = 'https://api.yelp.com/v3/businesses/search'
token = os.environ.get('yelp_token')
headers = {'Authorization' : token}

def get_restaurants(city, country):
    try:
        query = {'term': 'restaurants', 'location': f'{city} {country}', 'sort_by': 'rating', 'limit': 25}
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
    restaurant_list = []

    for restaurant in restaurant_data:
        if restaurant.location.city == city and restaurant.location.country == country:
            restaurant_list.append(restaurant)
            if len(restaurant_list) == 3:
                break

    return restaurant_list

data = get_restaurants('us', 'saint paul')
print(data)
restaurant_list = filter_restaurants('us', 'saint paul', data)
print(restaurant_list)