#!/usr/bin/python3
"""Fetch data from a url and POST."""
import requests
import sys


def fetch_url():
    """Fetch url and make POST request of values."""
    val = {}
    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) != 2):
        val['q'] = ""
    else:
        val['q'] = sys.argv[1]
    resp = requests.post(url, val)
    try:
        out = resp.json()
        if (out):
            print("[{}] <{}>".format(out['id'], out['name']))
        else:
            print("No result")
    except ValueError:
        print('Not a valid JSON')


if __name__ == "__main__":
    fetch_url()
