import requests
import os


url = "https://api.yelp.com/v3/businesses/search"
token = os.environ.get("yelp_token")
headers = {"Authorization": token}


def get_restaurants(city, country, result_limit):
    results = get_data(city, country, result_limit)
    filtered_results = filter_restaurants(city, country, results)
    restaurant_list = clean_up_restaurant_data(filtered_results)
    return restaurant_list


def get_data(city, country, result_limit):
    city = clean_up_input(city)
    country = clean_up_input(country)

    try:
        query = {
            "term": "restaurants",
            "location": f"{city}+{country}",
            "sort_by": "rating",
            "limit": result_limit,
        }
        response = requests.get(url, params=query, headers=headers)
        response.raise_for_status()
        data = response.json()
        data = data["businesses"]
        return data
    except Exception as ex:

        return []


def filter_restaurants(city, country, restaurant_data):
    city = clean_up_input(city)
    country = clean_up_input(country)
    restaurant_list = []

    for restaurant in restaurant_data:
        if (
            restaurant["location"]["city"].lower() == city
            and restaurant["location"]["country"].lower() == country
        ):
            restaurant_list.append(restaurant)
            if len(restaurant_list) == 3:
                break

    return restaurant_list


def get_categories(restaurant):
    categories = []
    for category in restaurant["categories"]:
        categories.append(category["title"])
    return categories


def clean_up_restaurant_data(restaurant_list):
    cleaned_list = []
    for restaurant in restaurant_list:
        restaurant_data = {
            "name": restaurant["name"],
            "url": restaurant["url"],
            "rating": restaurant["rating"],
            "categories": get_categories(restaurant),
        }
        cleaned_list.append(restaurant_data)

    return cleaned_list


def clean_up_input(text):
    return text.strip().lower()


if __name__ == "__main__":
    print()