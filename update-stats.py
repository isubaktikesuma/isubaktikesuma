import requests
import os
import re
from github import Github

README_PATH = "README.md"

# --- YouTube API ---
YT_API_KEY = os.getenv("YT_API_KEY")
CHANNEL_ID = "UCuTC7KIQxT5abBDwouY7FHA"  # Your channel ID

yt_url = (
    f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={YT_API_KEY}"
)

yt_data = requests.get(yt_url).json()
yt_subs = yt_data["items"][0]["statistics"]["subscriberCount"]
yt_views = yt_data["items"][0]["statistics"]["viewCount"]

# --- GitHub Traffic ---
g = Github(os.getenv("GH_TOKEN"))
repo = g.get_repo("isubaktikesuma/isubaktikesuma")
traffic = repo.get_views_traffic()
clones = repo.get_clones_traffic()

gh_views = traffic["count"]
gh_clones = clones["count"]

# --- Update README ---
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(r"{{YOUTUBE_SUBS}}", yt_subs, content)
content = re.sub(r"{{YOUTUBE_VIEWS}}", yt_views, content)
content = re.sub(r"{{GH_VIEWS}}", str(gh_views), content)
content = re.sub(r"{{GH_CLONES}}", str(gh_clones), content)

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(content)
