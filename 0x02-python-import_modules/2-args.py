#!/usr/bin/python3
if __name__ == "__main__":
    import sys
leng = (len(sys.argv) - 1)
if leng == 0:
    print("0 arguments.")
if leng == 1:
    print("1 argument:")
if leng > 1:
    print("{:d} arguments:".format(leng))
if leng:
    for i in range(1, leng + 1):
        print("{:d}:".format(i), sys.argv[i])
