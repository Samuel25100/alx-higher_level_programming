#!/bin/bash
# Take URL as argument and request to that URL and displays the size of the body
curl -s -w "%{size_download}\n" "$1"
