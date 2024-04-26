#!/usr/bin/python3
"""Fetch data from a url and POST."""
import requests
import sys


def fetch_url():
    """Fetch url and make POST request of values."""
    val = {}
    val["email"] = sys.argv[2]
    resp = requests.post(sys.argv[1], val)
    print(resp.text)


if __name__ == "__main__":
    fetch_url()
