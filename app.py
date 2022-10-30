from flask import Flask, redirect, render_template, request
import videos

# import restaurants, currency

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def homepage():
    return render_template("index.html")


@app.route("/travelguide", methods=["GET"])
def get_travel_info():

    home = request.args.get("country-from")
    country = request.args.get("country-destination")
    city = request.args.get("city-destination")

    videos = videos.youtube_search(city, country)

    return render_template(
        "travelguide.html",
        home="country-from",
        country=country,
        city=city,
        videos=videos,
    )


@app.route("/bookmarks")
def bookmark():
    return render_template("bookmarks.html")


#     if request.method == "get":


#     print(city)
#     print(country)
#     print(home)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
