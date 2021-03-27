# coding:utf-8

import sys


def func():
    while 1:
        line = sys.stdin.readline().strip()
        if not line:
            break
        print(line.split(" "))
        ls = list(map(int, line.split()))
        print(ls)


if __name__ == "__main__":
    # func()
    print(ascii(97))
    # ascii("a")
