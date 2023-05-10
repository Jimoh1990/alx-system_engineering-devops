#!/usr/bin/python3
"""
This script defines a function that queries the Reddit API
and prints the titles
of the first 10 hot posts for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Recursively get all hot article titles for a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    articles = data.get("data", {}).get("children", [])

    for article in articles:
        title = article.get("data", {}).get("title", "")
        hot_list.append(title)

    after = data.get("data", {}).get("after", None)

    if after is not None:
        return recurse(subreddit, hot_list, after=after)
    return hot_list
