# -*- coding:utf-8 -*-
# Created data: 20200721


# 回溯的思路
# https://leetcode-cn.com/problems/subsets/solution/hui-su-si-xiang-tuan-mie-pai-lie-zu-he-zi-ji-wen-t/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rt = [[]]
        n = len(nums)
        def search(left, ls):
            rt.append(ls.copy())
            if left == n-1: return
            # ls.append(nums[ls])
            for i in range(left+1, n):
                ls.append(nums[i])
                search(i, ls)
                ls.pop(-1)

        for i in range(0, n):
            search(i, [nums[i]])
        return rt


nums = [1, 2, 3]
s = Solution()
rt = s.subsets(nums)
print(rt)

"""
# 39.组合总和
40. 组合总和 II
# 46. 全排列
47. 全排列 II
78. 子集
90. 子集 II
"""
