#!/bin/bash
# Take URL as argument and make HEADER request
curl -iX POST -d "@$2" -H "Content-Type: application/json" "$1"
