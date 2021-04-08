#!/bin/bash
# this is a comment
curl "$1" -sI | grep "Allow" | cut -d " " -f 2-
