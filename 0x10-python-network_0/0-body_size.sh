#!/bin/bash
# Take URL as argument and request to that URL and displays the size of the body
curl -s "$1" | wc -c
