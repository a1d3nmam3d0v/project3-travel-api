import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pprint import pprint

# required arguments to pass to the build function
DEVELOPER_KEY = os.environ.get("YOUTUBE_API_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def get_videos(city, country):

    search_string = f"{city},{country} travel tour"

    if not DEVELOPER_KEY:
        return "Missing API key"

    youtube = build(
        YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY
    )

    # call search.list method to retrieve results
    response = (
        youtube.search()
        .list(
            part="id,snippet",
            q=search_string,
            type="video",
            maxResults=3,
            # fields="items(id(videoId), snippet(title))",
        )
        .execute()
    )
    
    results = response.get("items", [])

    for result in results:

        vids = {
            "title": result["snippet"]["title"],
            "video_id": result["id"]["videoId"],
        }
        pprint(vids)
        return vids


if __name__ == "__main__":
    youtube_search("las vegas", "united states")
