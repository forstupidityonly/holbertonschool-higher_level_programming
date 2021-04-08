#!/bin/env bash
# this is a comment
curl -sI "$1"|awk '/Content-Length/{print $2}'