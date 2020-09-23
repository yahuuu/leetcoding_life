# -*- coding:utf-8 -*-
# Created data: 2020


import sys

# target = sys.stdin.readline().strip()
# str1 = sys.stdin.readline().strip()
target = "hello "
str1 = "hello world"

def solution():
    num_str = len(str1)
    num_t = len(target)
    i = 0
    j = 0
    for _ in range(num_str):
        if target[i] == str1[j]:
            i += 1
            j += 1
            if i == num_t:
                return 1
        else:
            i = 0
            j += 1
    return 0


solu = solution()
print(solu)
