import os
import requests

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# key = 'AIzaSyDE-Mcze5lzysMagAiik1MgrGUjLGkqdxw'
DEVELOPER_KEY = os.environ.get("YOUTUBE_API_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(city, country):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY
    )

    destination_name = f"{city} {country} tour"

    search_response = (
        youtube.search()
        .list(
            q=destination_name,
            part="id, snippet",
            maxResults=3,
        )
        .execute()
    )

    videos = []

    for search_result in search_response.get("items", []):

        title = search_result["snippet"]["title"]
        video_id = search_result["id"]["videoId"]

        return {"title": title, "video_id": video_id}

    #     videos.append(
    #         "%s (%s)"
    #         % (search_result["snippet"]["title"], search_result["id"]["videoId"])
    #     )

    # print("Videos:\n", "\n".join(videos), "\n")


if __name__ == "__main__":
    youtube_search(city, country)
