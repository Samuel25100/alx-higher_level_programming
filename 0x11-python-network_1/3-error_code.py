#!/usr/bin/python3
"""Fetch data from a url and handle error."""
import urllib.request
import urllib.error
import sys


def fetch_url():
    """Fetch id value of X-request-Id from header."""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            file = response.read()
            print(file.decode('utf-8'))
    except urllib.error.HTTPError as er:
        print("Error code: ", er.code)


if __name__ == "__main__":
    fetch_url()
