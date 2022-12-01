#!/usr/bin/python3
import sys

count = len(sys.argv) - 1

if count == 0:
    print(f"{count} arguments")
else:
    print(f"{count} arguments")

for i in range (1, count + 1):
    print("{}: {}".format(i, (sys.argv[i])))
