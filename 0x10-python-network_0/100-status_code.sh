#!/bin/bash
# Take URL as argument and make HEADER request
curl -sw "%{http_code}" "$1"
