#!/usr/bin/python3
"""

Recursive function that queries the Reddit API and
returns a list titles of all
hot articles for a  su

"""
import requests


def recurse(su, ht=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(su)
    params = {
        "after": after
    }
    req = requests.get(
        url, headers={'User-Agent': 'Python/requests'}, params=params)
    try:
        resp = req.json()
        posts = resp.get("data", {}).get("children", None)
        after = resp.get("data", {}).get("after", None)
        if posts is not None:
            [ht.append(post.get("data").get("title")) for post in posts]
        if after is None:
            if len(ht) == 0:
                return None
            return ht
        else:
            return recurse(su, ht, after=after)

    except Exception:
        return None