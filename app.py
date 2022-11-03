from flask import Flask, redirect, render_template, request, url_for

import currency
import restaurants
import videos
from currency_map import country_to_currency, get_full_country_name

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/travelguide", methods=["GET", "POST"])
def get_travel_info():
    # From the form input that the submits
    home_countrycode = request.args.get("country-from")
    destination_countrycode = request.args.get("country-destination")
    city = request.args.get("city-destination").capitalize()
    destination_country_full_name = get_full_country_name(destination_countrycode)
    home_country_full_name = get_full_country_name(home_countrycode)

    # Conveting from 2 letter cc to 3 letter currency code
    home_currency = country_to_currency(get_full_country_name(home_countrycode))
    destination_currency = country_to_currency(
        get_full_country_name(destination_countrycode)
    )
    # Calling the APIs
    money = currency.get_exchange_rate(home_currency, destination_currency)
    food = restaurants.get_restaurants(city, destination_countrycode, 20)
    vids = videos.get_videos(city, destination_country_full_name)

    return render_template(
        "travelguide.html",
        home_countrycode=home_countrycode,
        destination_country_full_name=destination_country_full_name,
        home_country_full_name=home_country_full_name,
        city=city,
        vids=vids,
        food=food,
        money=money,
        # fullname_country_destination=fullname_country_destination
    )


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/save", methods=["POST"])
def save(methods=["POST"]):
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


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404