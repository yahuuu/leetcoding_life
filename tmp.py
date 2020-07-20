# -*- coding:utf-8 -*-
# Created data:


ls = [1,2,3,4,5,6,7,8]
# O(n**2)

def solution(ls):
    for i in range(0, len(ls), 1):
        if ls[i]%2 == 1:
            ls.remove(ls[i])
            ls.append(ls[i])
        # else: pass


def solution3(ls):
    d = 0; s = len(ls)-1
    while True:
    # while d < s:
        while ls[d]%2 == 0: # and d < s:
            d += 1
        while ls[s]%2 == 1: # and d < s:
            s -= 1
        if d >= s: break
        ls[d], ls[s] = ls[s], ls[d]
        d += 1; s -= 1

solution3(ls)
print(ls)