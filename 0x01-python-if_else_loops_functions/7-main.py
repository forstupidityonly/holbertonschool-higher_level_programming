#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("i is {}".format("lower" if islower("i") else "upper"))
print("Y is {}".format("lower" if islower("Y") else "upper"))
print("G is {}".format("lower" if islower("G") else "upper"))
print("2 is {}".format("lower" if islower("2") else "upper"))
print("k is {}".format("lower" if islower("k") else "upper"))
