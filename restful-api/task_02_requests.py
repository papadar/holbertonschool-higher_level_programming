#!/usr/bin/python3
"""request posts from url - print and save responses"""
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """fetch the posts, print the titles & status codes"""
    response = requests.get(url, timeout=10)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """fetch the posts, store elements in a csv table"""
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
