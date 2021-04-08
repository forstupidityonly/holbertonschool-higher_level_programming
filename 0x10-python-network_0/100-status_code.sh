#!/bin/bash
# a comment for checker
curl -sL -o /dev/null -I -w "%{http_code}" "$1"