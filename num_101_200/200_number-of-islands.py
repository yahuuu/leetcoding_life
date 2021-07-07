# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 上午8:30
# @Author  : yahuuu
# @FileName: 200_number-of-islands.py
# @Software: PyCharm

"""先想好思路，
DFS，找到岛屿，优先深度遍历相邻四个点，把可能的相连岛屿全部标记为水，
之后遍历所有元素时候，之前的岛屿就可以略过了。
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.w = len(grid)
        self.h = len(grid[0])
        self.num = 0
        self.grid = grid
        for i in range(self.w):
            for j in range(self.h):
                if self.grid[i][j] == "1":
                    self.num += 1
                    self.search(i, j)
        return self.num

    def search(self, m, n):
        # 防止岛屿索引直接变负数
        # if m >= self.w or n >= self.h or m < 0 or n < 0 or self.grid[m][n] == "0":
        if (not 0 <= m < self.w) or (not 0 <= n < self.h) or self.grid[m][n] == "0":
            return
        self.grid[m][n] = "0"
        self.search(m + 1, n)
        self.search(m - 1, n)
        self.search(m, n + 1)
        self.search(m, n - 1)


# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# grid = [["1", "0", "1", "1", "0", "1", "1"]]