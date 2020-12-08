#!/usr/bin/python3
for j in range(97, 123):
    if j == 'q' or j == 'e':
        continue
    else:
        print("{:c}".format(j), end='')
