# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 上午8:18
# @Author  : yahuuu
# @FileName: 338_counting-bits.py
# @Software: PyCharm


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        ls = [0]*(n+1)
        for i in range(n+1):
            ls[i] = str(bin(i))[2:].count("1")

        return ls