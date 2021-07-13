# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 上午8:18
# @Author  : yahuuu
# @FileName: 338_counting-bits.py
# @Software: PyCharm

from typing import List

class Solution1:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        ls = [0]*(n+1)
        for i in range(n+1):
            ls[i] = str(bin(i))[2:].count("1")
        return ls


# https://leetcode-cn.com/problems/counting-bits/solution/yi-bu-bu-fen-xi-tui-dao-chu-dong-tai-gui-3yog/
# 动态规划不是拍脑袋想出来的，递归->记忆递归->动态规划。
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        if n == 1: return [0, 1]
        ls = [0 for i in range(n+1)]
        ls[1] =1
        for i in range(2, n+1):
            ls[i] = (i&0x01) + ls[i>>1]
        return ls


solu = Solution()
print(solu.countBits(3))
