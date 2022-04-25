#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/25
# @Author  : yahuuu

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f, n, numSum = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            f += i * num
        res = f
        for i in range(n - 1, 0, -1):
            f = f + numSum - n * nums[i]
            res = max(res, f)
        return res


nums = [4,3,2,6]
solu = Solution()
res = solu.maxRotateFunction(nums)
print(res)
