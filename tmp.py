# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 上午9:45
# @Author  : yahuuu
# @FileName: tmp.py
# @Software: PyCharm



ls1 = ["a", "b", "c", "d"]
class Solution():
    def __init__(self):
        self.ls = []

    def helper(self, ls, idls, id, limit):
        if len(ls) == limit:
            self.ls.append((ls[:], idls[:]))
            return
        for i in range(id, self.n):
            ls.append(ls1[i])
            idls.append(i)
            self.helper(ls, idls, i+1, limit)
            ls.pop(-1)
            idls.pop(-1)

    def backtracking(self):
        self.n = len(ls1)
        self.limit = 2
        for limit in range(1, len(ls1)):
            self.helper([], [], 0, limit)

solu = Solution()
solu.backtracking()
print(solu.ls)

