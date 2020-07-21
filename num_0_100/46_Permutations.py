# -*- coding:utf-8 -*-
# Created data: 20200721


# 递归回溯算法
class Solution:
    def permute(self, nums):  # List[int]) -> List[List[int]]:
        rt = []
        n = len(nums)
        def helper(left):
            # 出栈点
            if left == n:
               rt.append(nums[:])  # copy 记录
            for i in range(left, len(nums), 1):
                nums[left], nums[i] = nums[i], nums[left]
                # 下一个递归点
                helper(left + 1)
                # 回溯, 恢复状态
                nums[left], nums[i] = nums[i], nums[left]
        helper(0)
        return rt


nums = [1, 2, 3, 4]
s = Solution()
rt = s.permute(nums)
print(rt)


"""
# 39.组合总和
40. 组合总和 II
# 46. 全排列
47. 全排列 II
78. 子集
90. 子集 II
"""
