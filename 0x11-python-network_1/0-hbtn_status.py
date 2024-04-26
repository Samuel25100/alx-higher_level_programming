#!/usr/bin/python3
"""Fetch data from a url."""
import urllib.request


def fetch_url():
    """Fetch data from url."""
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        file = response.read()
        print("Body response:")
        print("\t- type:", type(file))
        print("\t- content:", file)
        print("\t- utf8 content:", file.decode("utf-8"))


if __name__ == "__main__":
    fetch_url()
