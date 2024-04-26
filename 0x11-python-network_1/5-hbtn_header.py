#!/usr/bin/python3
"""Fetch data from a url."""
import requests
import sys


def fetch_url():
    """Fetch id value of X-request-Id from header."""
    file = requests.get(sys.argv[1])
    file = file.headers
    print(file['X-Request-Id'])


if __name__ == "__main__":
    fetch_url()
