# coding:utf-8
# Code date: 20200902

from typing import List

# 这样的题目我先想到就是递归，
# 差一个用例通过，时间最后还是超限制了，哈哈
# 必须玩动态规划了，这道题，剪枝失效
# O(2*N^2)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_path = float("inf")
        row = len(triangle)
        def helper(path, idx, step):
            nonlocal min_path
            if step == row-1:
                min_path = min(min_path, sum(path))
                return
            # 有时候剪枝是错误的，如出现负数，部分路径的和有可能大于临时最小值
            # 如果元素都是大于零，那么剪枝是很有意义
            # elif sum(path)>min_path:  # prune
            #     return

            path.append(triangle[step+1][idx])
            helper(path, idx, step+1)
            path.pop(-1)

            path.append(triangle[step+1][idx+1])
            helper(path, idx+1, step+1)
            path.pop(-1)

        helper([triangle[0][0]], idx=0, step=0)
        return min_path

# 动态规划的思路是从下到上依次计算路径
# 递归是记录路径，并且需要回溯，入栈出栈也会消耗时间
# 参考自
# https://leetcode-cn.com/problems/triangle/solution/pythonzui-jian-ji-dai-ma-onhe-o1kong-jian-liang-ch/
class Solution_ogami1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
        return dp[0]
# ogami 时间O(N^2)
# 直接操作原矩阵，空间O(1)
class Solution_ogami2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2,-1,-1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]


triangle = [
    [2],
    [3, 14],
    [6, 6, 0],
    [2, 1, 1, 8]
]
# triangle = [
#              [-1],
#              [2, 3],
#              [1, -1, -3]
# ]
solu = Solution_ogami2()
min_path = solu.minimumTotal(triangle)
print(min_path)