#!/usr/bin/python3
import sys
num = 0
for i in range(1, len(sys.argv)):
    num += int(sys.argv[i])
print("{:d}".format(num))
