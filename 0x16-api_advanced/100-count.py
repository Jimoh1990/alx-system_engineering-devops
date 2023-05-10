#!/usr/bin/python3
"""
Count occurrences of keywords in Reddit posts
"""

import requests


def count_words(subreddit, word_list, count_dict=None, after=None):
    """
    Recursive function that queries the Reddit API and counts the
    number of times
    the given keywords appear in the titles of all hot articles for
    a given subreddit.The counts are case-insensitive and words that
    are duplicates of the same word (case-insensitive)
    should be counted together.
    """

    # If count_dict is None, create an empty dictionary for counting words.
    if count_dict is None:
        count_dict = {}

    """
    Base case: If subreddit is not valid or there are no more articles,
    return the count_dict.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after} if after else None
    response = requests.get(url, headers=headers, params=params,
            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")
    if not data:
        return count_dict

    """
    Recursive case: Parse the titles of all hot articles and
    update the count_dict with the keyword counts.
    """
    children = data.get("children")
    for child in children:
        title = child.get("data").get("title").lower()
        for word in word_list:
            if title.count(word.lower()):
                count_dict[word.lower()] = count_dict.get(word.lower(),
                        0) + title.count(word.lower())

    # Recursively call the function with the next page of results.
    count_words(subreddit, word_list, count_dict, data.get("after"))

    # Return the count_dict when all the pages have been processed.
    if not after:
        for word, count in sorted(count_dict.items(), key=lambda
                    x: (-x[1], x[0])):
            print(f"{word}: {count}")
