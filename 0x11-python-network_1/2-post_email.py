#!/usr/bin/python3
"""Fetch data from a url and POST."""
import urllib.request
import urllib.parse
import sys


def fetch_url():
    """Fetch url and make POST request of values."""
    val = {}
    val["email"] = sys.argv[2]
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    resp = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(resp) as response:
        file = response.read()
        print(file.decode('utf-8'))


if __name__ == "__main__":
    fetch_url()
