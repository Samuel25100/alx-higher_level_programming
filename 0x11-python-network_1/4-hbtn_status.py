#!/usr/bin/python3
"""Fetch data from a url."""
import requests


def fetch_url():
    """Fetch data from url using requests package."""
    url = "https://alx-intranet.hbtn.io/status"
    with requests.get(url) as file:
        print("Body response:")
        print("\t- type:", type(file.text))
        print("\t- content:", file.text)


if __name__ == "__main__":
    fetch_url()
