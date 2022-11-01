import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pprint import pprint
import json

# required arguments to pass to the build function
DEVELOPER_KEY = os.environ.get("YOUTUBE_API_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def get_videos(city, country):

    search_string = f"{city},{country} travel tour"

    # if not DEVELOPER_KEY:
    #     return "Missing API key"

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
            fields="items(id(videoId), snippet(title))",
        )
        .execute()
    )

    # vids = {"title": [], "id": []}

    for item in response["items"]:
        
        videoId = item["id"]["videoId"]
        title = item["snippet"]["title"]
        
        
        
        # vids["title"].append(title)
        # vids["id"].append(videoId)
        
        # return {"title": title, ["id"]: id}
    
    # for result in results:

        # vids = {
        #     "title": response["snippet"]["title"],
        #     "video_id": response["id"]["videoId"],
        #     }
    
        pprint(vids)


        
        pprint(vids)
        return vids


# results = response.get("items", [])
# results = response.get("items")

# items = response["items"]
# if not items:
#     return "No youtube videos"

# title = items["snippet"]["title"]
# video_id = items["id"]["videoId"]

# videos = {"title": title, "videoId": video_id}

# print(vids)
# return {'vids'}

# for result in results:

# vids = {
#     "title": result["snippet"]["title"],
#     "video_id": result["id"]["videoId"],
# }

# return vids
# pprint(vids)


if __name__ == "__main__":
    get_videos("las vegas", "united states")
