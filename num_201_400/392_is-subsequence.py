# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 上午8:20
# @Author  : yahuuu
# @FileName: 392_is-subsequence.py
# @Software: PyCharm

class Solution0:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        slen = len(s)
        tlen = len(t)
        i = 0; j = 0
        while (i < slen and j < tlen):
            if s[i] == t[j]:
                i += 1
            j += 1
            if i == slen:
                return True
        return False