#!/usr/bin/python3
"""Fetch data from a url."""
import urllib.request
import sys


def fetch_url():
    """Fetch id value of X-request-Id from header."""
    with urllib.request.urlopen(sys.argv[1]) as response:
        file = response.headers
        print(file["X-Request-Id"])


if __name__ == "__main__":
    fetch_url()
