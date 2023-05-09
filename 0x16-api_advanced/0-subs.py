#!/usr/bin/python3
"""
Function that queries the Reddit API and
returns number of subscribers
for a subreddit
"""
import requests


def number_of_subscribers(su):
    url = "https://www.reddit.com/r/{}/about.json".format(su)
    req = requests.get(url, headers={'User-Agent': 'Python/requests'})

    try:
        resp = req.json()
        return resp.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
