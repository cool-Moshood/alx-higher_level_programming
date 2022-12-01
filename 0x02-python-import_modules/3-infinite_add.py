#!/usr/bin/python3
import sys
if __name__ == "__main__":

    add = 0
    count = len(sys.argv) - 1
    if count != 0:

        for i in range(1, count + 1):
            add += int(sys.argv[i])
        print(f"{add}")

    else:
        print(count)
