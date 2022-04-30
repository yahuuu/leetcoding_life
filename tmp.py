# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 上午9:45
# @Author  : yahuuu
# @FileName: tmp.py
# @Software: PyCharm

from typing import List

class Solution:
    def __init__(self):
        self.res = list()
        self.records = None
        self.n = 0

    def helper(self, nums, ls: List):
        if len(ls) == self.n:
            self.res.append(ls.copy())
        for i in range(self.n):
            if self.records[i] == 0:
                # ls.append(nums[i])
                self.records[i] = 1
                self.helper(nums, ls+[nums[i]])
                # ls.pop(-1)
                self.records[i] = 0

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.records = [0 for i in nums]
        self.helper(nums, [])
        return self.res

if __name__ == '__main__':
    # nums = [ 1]
    nums = [ 1, 2, 3]
    solu = Solution()
    res = solu.permute(nums)
    print(res)