from urllib import response
import requests

url = 'https://api.yelp.com/v3/businesses/search'
token = 'bearer yh7Lwck6xLvgxlOXM2y21vf-ZRF2FLI71uHf49D0wQs5-t732nOCrzpZAwo-__-nZpeawllILeMHgFNP-eE1RLc1u8xHOYxDgM12iBL_pvx-m9SPDbQsbU0WIMycX3Yx'
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
    








   


