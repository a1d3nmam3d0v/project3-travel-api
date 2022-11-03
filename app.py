from flask import Flask, redirect, render_template, request, url_for

import videos, restaurants, currency
from currency_map import get_full_country_name, country_to_currency


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/travelguide", methods=["GET", "POST"])
def get_travel_info():
    form_data = request.args
    home = form_data.get("country-from")
    country = form_data.get("country-destination")
    city = form_data.get("city-destination")

    food = restaurants.get_restaurants(city, country, 20)
    print("RESTAURANTS HERE")
    print(food)

    home_currency = country_to_currency(get_full_country_name(home))
    destination_currency = country_to_currency(get_full_country_name(country))

    vids = videos.get_videos(city, country)

    money = currency.get_exchange_rate(home_currency, destination_currency)

    return render_template(
        "travelguide.html",
        home=home,
        country=country,
        city=city,
        vids=vids,
        food=food,
        money=money,
    )


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/save", methods=["POST"])
def save():
    saved_item = request.form["name"]
    saved_item = request.form["url"]
    saved_item = request.form["country"]
    saved_item = request.form["city"]
    saved_item = request.form["type"]

    return redirect(url_for("bookmark"))


@app.route("/bookmark")
def bookmark():
    return render_template("bookmarks.html")


if __name__ == "__main__":
    app.run(debug=True)
