#!/bin/bash
# Take URL as argument and make HEADER request
curl -siX POST -d "@$2" -H "Content-Type: application/json" "$1" | tail -n 1
