#!/bin/bash
# Bash script that sends a DELETE request to the URL
curl -sIX OPTIONS "$1" | awk -F': ' '/Allow/ { print $2 }'
