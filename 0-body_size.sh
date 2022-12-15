#!/bin/bash
# takes in a URL, sends request to URL, displaying the size of the body of the response
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
