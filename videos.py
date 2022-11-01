import os
import json
import pprint

import requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# dev key is AIzaSyDE-Mcze5lzysMagAiik1MgrGUjLGkqdxw

# required arguments for the build function
DEVELOPER_KEY = os.environ.get("YOUTUBE_API_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creates Youtube object
youtube = build(
    YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY
)


def youtube_search(city, country):
    # uses input from the form as the search keyword
    destination = f"{city} {country} tour"

    # search.list method is called to retrieve results
    search_response = (
        youtube.search()
        .list(
            q=destination,
            part="id,snippet",
            maxResults=3,
            type="video",
        )
        .execute()
    )

    results = search_response.get("items", [])

    for result in results:

        vids = {
            "title": result["snippet"]["title"],
            "video_id": result["id"]["videoId"],
        }

        return vids


# if __name__ == "__main__":
#     youtube_search("las vegas", "united states")
