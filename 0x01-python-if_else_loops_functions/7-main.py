#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("i is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("Y is {}".format("lower" if islower("3") else "upper"))
print("Q is {}".format("lower" if islower("g") else "upper"))
