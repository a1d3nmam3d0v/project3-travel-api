import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Needed for Google's build function
DEVELOPER_KEY = os.environ.get("YOUTUBE_API_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def get_videos(city, country):

    if not DEVELOPER_KEY:
        return "Missing API key"
    # The search query for Youtube
    search_string = f"{city},{country} travel tour"

    youtube = build(
        YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY
    )

    # Search.list method retrieves API results
    response = (
        youtube.search()
        .list(
            q=search_string,
            type="video",
            part="id,snippet",
            maxResults=3,
            # fields="items(id(videoId), snippet(title))",
        )
        .execute()
    )

    results = response.get("items")
    if not results:
        return []

    vids = []
    for result in results:

        title = result["snippet"]["title"]
        videoId = result["id"]["videoId"]
        url = f"https://youtu.be/{videoId}"

        videos = {"title": title, "videoId": videoId, "url": url}

        vids.append(videos.copy())

    return vids


if __name__ == "__main__":
    get_videos("Minneapolis", "United States")
