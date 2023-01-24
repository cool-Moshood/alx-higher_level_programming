#!/usr/bin/python3
""" 1-main """
from models.square import Square

if __name__ == "__main__":

    # s1 = Square(5)
    # print(s1)
    # print(s1.size)
    # s1.size = 10
    # print(s1)

    # try:
    #     s1.size = "9"
    # except Exception as e:
    #     print("[{}] {}".format(e.__class__.__name__, e))


    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)