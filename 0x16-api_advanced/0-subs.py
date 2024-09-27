#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    # Set the base URL for the subreddit's about.json endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Define custom headers to avoid the Too Many Requests error (including a User-Agent)
    headers = {
        "User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/frowningheart)"
    }

    try:
        # Make the GET request and ensure no redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the request is successful and returns a valid response, extract subscriber count
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            # If subreddit is invalid or request fails, return 0
            return 0

    except requests.RequestException:
        # Catch any exceptions during the request and return 0
        return 0


# Example usage:
# print(number_of_subscribers('python'))  # Example of a valid subreddit
# print(number_of_subscribers('thissubredditdoesnotexist'))  # Example of an invalid subreddit
