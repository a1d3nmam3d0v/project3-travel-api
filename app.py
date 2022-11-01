from flask import Flask, redirect, render_template, request, jsonify
import videos
import restaurants, currency

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def homepage():
    return render_template("index.html")


@app.route("/travelguide", methods=["GET", "POST"])
def get_travel_info():
    form_data = request.args
    home = form_data.get("country-from")
    country = form_data.get("country-destination")
    city = form_data.get("city-destination")

    vids = videos.youtube_search(city, country)
    title = vids.get("title")
    video_id = vids.get("video_id")

    return render_template(
        "travelguide.html",
        home=home,
        country=country,
        city=city,
        vids=vids,
        title=title,
        video_id=video_id,
    )


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/bookmarks")
def bookmark():
    return render_template("bookmarks.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
