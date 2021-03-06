# -*- coding:utf-8 -*-
# Created data: 20200721


# 递归回溯算法
class Solution_org:
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

# 这是记录路径不交换元素的方式，这样需要维护一个使用表
# 这里没有剪枝
class Solution_nocut:
    def permute(self, nums):  # List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0: return []
        rt = []

        def helper(left, path, used):
            if len(path) == n:
                rt.append(path[:])
            for i in range(0, n):
                if used[i]: continue
                path.append(nums[i])
                used[i] = True
                helper(left+1, path, used)
                path.pop(-1)
                used[i] = False
        helper(0, [], [False for _ in range(len(nums))] )
        return rt


class Solution:
    def permute(self, nums):  # List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0: return []
        rt = []

        def helper(left, path, used):
            if len(path) == n:
                rt.append(path[:])
            for i in range(0, n):
                if used[i]: continue
                path.append(nums[i])
                used[i] = True
                helper(left+1, path, used)
                path.pop(-1)
                used[i] = False
        helper(0, [], [False for _ in range(len(nums))] )
        return rt

nums = [1, 2, 3]
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
