#!/usr/bin/python3
"""request posts from url - print and save responses"""
import requests

url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """fetch the posts, print the titles & status codes"""
    response = requests.get(url, timeout=10)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
