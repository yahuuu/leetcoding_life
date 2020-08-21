# -*- coding:utf-8 -*-
# Created data: 20200721


# 题解：dfs+traceback
# 递归回溯算法
# 这道题，是一颗树状结构，但是和之前做的递归树不同点在于要不断的交换元素，
# 在写这道题之前最好先花一棵树，才知道如何dfs如何回溯,如何剪枝
class Solution_nocut:
    def permute(self, nums):  # List[int]) -> List[List[int]]:
        rt = []
        n = len(nums)
        def helper(left):
            # 出栈点
            if left == n:
                rt.append(nums[:])  # copy 记录
                print(nums)
            for i in range(left, len(nums), 1):
                nums[left], nums[i] = nums[i], nums[left]
                # 下一个递归点
                helper(left + 1)
                # 回溯, 恢复状态
                nums[left], nums[i] = nums[i], nums[left]
        helper(0)
        return rt


class Solution_nocut1:
    def permute(self, nums):  # List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0: return []
        rt = []
        def permu(left):
            if left == n:
                rt.append(nums.copy())
            for i in range(left, n, 1):
                if left != i:  # 只是跳过，不算剪枝
                    nums[left], nums[i] = nums[i], nums[left]
                permu(left+1)
                if left != i:
                    nums[left], nums[i] = nums[i], nums[left]
        permu(left=0)
        return rt


# 一个新的对象，可以支持新特性
from typing import List

# 这是网友的解法
# 重点这里剪枝
# 和我的思路不同的地方是，这里需要维护一个列表，
# 每次递归都是记录路径，

class Solution30:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]

        self.backtrack([], nums, check)
        return self.res

    def backtrack(self, path, nums, used):
        if len(path) == len(nums):
            self.res.append(path)
            return

        for i in range(len(nums)):
            if used[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i-1] and used[i - 1] == 0:
                continue
            used[i] = 1
            self.backtrack(path+[nums[i]], nums, used)
            used[i] = 0


nums = [1, 1, 2]
s = Solution30()
rt = s.permuteUnique(nums)
print(rt)


"""
# 39.组合总和
40. 组合总和 II
# 46. 全排列
47. 全排列 II
78. 子集
90. 子集 II
"""
