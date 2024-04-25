#!/bin/bash
# Take URL as argument and make GET request
curl -sI "$1" | grep "Allow" | cut -d ' ' -f 2-
