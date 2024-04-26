#!/usr/bin/python3
"""Fetch data from a url and handle error."""
import requests
import sys


def fetch_url():
    """Fetch id value of X-request-Id from header."""
    file = request.get(sys.argv[1])
    if (file.status_code >= 400):
        print("Error code:", file.status_code)
    else:
        print(file.text)


if __name__ == "__main__":
    fetch_url()
