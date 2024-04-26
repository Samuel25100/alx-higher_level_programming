#!/usr/bin/python3
"""Fetch data from a url."""
import urllib.request

def fetch_url():
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        file = response.read()
        print(file.decode("utf-8"))

if __name__ == "__main__":
    fetch_url()
