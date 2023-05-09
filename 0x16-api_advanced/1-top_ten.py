#!/usr/bin/python3
"""
Function that querie Reddit API and
prints titles first 10 hot posts listed
for given su
"""
import requests


def top_ten(su):
    url = "https://www.reddit.com/r/{}/hot.json".format(su)
    params = {
        'limit': 10
    }
    req = requests.get(
        url, headers={'User-Agent': 'Python/requests'}, params=params)

    try:
        resp = req.json()
        posts = resp.get("data", {}).get("children", None)
        if posts is None:
            print(None)
        else:
            [print(post.get("data").get("title")) for post in posts]
    except Exception:
        print(None)