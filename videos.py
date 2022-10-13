import os
import requests

# key = 'AIzaSyDE-Mcze5lzysMagAiik1MgrGUjLGkqdxw'


key = os.environ.get("YOUTUBE_API_KEY")
query = {}
YOUTUBE_API_KEY = "AIzaSyDE-Mcze5lzysMagAiik1MgrGUjLGkqdxw"

url = "GET https://www.googleapis.com/youtube/v3/videos"
