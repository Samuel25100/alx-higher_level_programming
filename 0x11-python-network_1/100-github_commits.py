#!/usr/bin/python3
"""Fetch data from a url from github api."""
import requests
import sys


def fetch_url():
    """Fetch data from github api using usename and password."""
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[1], sys.argv[2])
    try:
        resp = requests.get(url, params={'per_page': 10})
        val = resp.json()
        for i in val:
            print("{}: {}".format(
                i["sha"],
                i["commit"]["author"]["name"]))
    except (IndexError, ValueError):
        pass


if __name__ == "__main__":
    fetch_url()
