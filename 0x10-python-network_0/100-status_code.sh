#!/bin/bash
# a comment for checker
curl -sLo /dev/null -s -w "%{http_code}" "$1"