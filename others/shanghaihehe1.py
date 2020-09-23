# -*- coding:utf-8 -*-
# Created data: 2020
from collections import deque


# binary search , O(logN)
import sys

# test
ls = [1,2,3,3,4,5]
target = 1
num = 6

def get_num():
    global target
    target = int(sys.stdin.readline().strip())
    # print(target)
    global num
    num = int(sys.stdin.readline().strip())

    for _ in range(num):
        global ls
        ele = int(sys.stdin.readline().strip())
        ls.append(ele)
    # print(ls)


def hori_search(idx):
    if idx == -1:
        return -1
    if idx == num-1:
        return num-1
    tmp = None
    for i in range(idx+1, num):
        if ls[i] == target:
            pass
        else:
            tmp = i-1
            break
    return tmp


def binary_search():
    global num
    if num == 0:
        return -1
    begin = 0
    end = num-1
    while begin <= end:
        mid = (begin+end)//2
        if ls[mid] == target:
            # return hori_search(mid)
            return mid # just a tmp result
        elif ls[mid] < target:
            begin = mid+1
        elif ls[mid] > target:
            end = mid-1
    return -1


# get_num()
res = binary_search()
res = hori_search(res)
sys.stdout.write(str(res))







