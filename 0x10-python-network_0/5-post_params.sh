#!/bin/bash
# Take URL as argument and make HEADER request
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
