#!/usr/bin/python3
"""
Defines the top_ten function
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a
    given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in data:
            print(post.get('data').get('title'))
    else:
        print(None)
