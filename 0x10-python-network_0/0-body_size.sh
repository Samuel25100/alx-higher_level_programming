#!/usr/bin/bash
# Take URL as argument and request to that URL and displays the size of the body
size=$(curl -s -w "%{size_download}" "$1")
echo "$size"
