#!/usr/bin/python3
"""Fetch data from a url and POST."""
import requests
import sys


def fetch_url():
    """Fetch data from github api using usename and password."""
    url = "https://api.github.com/user"
    resp = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    val = resp.json()
    print(val.get("id"))


if __name__ == "__main__":
    fetch_url()
