# coding:utf-8
# Code date: 20200901

from typing import List

# 递归树再次时间超出限制，需要剪枝,剪枝后多通过5个用例，看来递归树搞不定了。
# 得用动态规划！！
# 要么向右移动要么向左移动
# 我的出发点是从左上角到右下角
# 官方动态规划是从右下角到左上角
class Solution1:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.row = len(grid)-1
        self.col = len(grid[0])-1
        self.min = float("inf")

        def helper(m, n, path_ls):
            # 回溯
            path_ls = path_ls[0:m + n + 1]  # 加这行的原因是因为，我的回溯没处理好，因此按照数量切片
            if sum(path_ls) > self.min:  # 剪枝，当前路径和已经大于最小值了，返回吧
                return
            if m > self.row or n > self.col:  # exit of stack
                return
            path_ls.append(grid[m][n])
            if m == self.row and n == self.col:
                self.min = min(self.min, sum(path_ls))
            else:
                helper(m, n + 1, path_ls)
                helper(m + 1, n, path_ls)
                # path_ls.pop(-1)
                # path_ls.pop(-1)

        helper(0, 0, [])
        return self.min


# 这里思路和上边一样，先向矩阵右边走，然后向矩阵下边走，
# 这里回溯的处理方法不同，也更合理，
# 这次在处理边界时候，不会让超限制
class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.row = len(grid)-1
        self.col = len(grid[0])-1
        self.min = float("inf")
        def helper(m, n, path_ls):
            if sum(path_ls) > self.min:  # 剪枝，当前路径和已经大于最小值了，返回
                return
            if m == self.row and n == self.col:
                self.min = min(self.min, sum(path_ls))
            else:
                # 先向右边走
                if n<self.col:  # 不会超边界了，
                    path_ls.append(grid[m][n+1])
                    helper(m, n + 1, path_ls)
                    path_ls.pop(-1)  # 回溯

                if m<self.row:
                    path_ls.append(grid[m+1][n])
                    helper(m + 1, n, path_ls)
                    path_ls.pop(-1)   # 回溯
        helper(0, 0, [grid[0][0]] )
        return self.min


# TODO：用动态规划写下吧
# 路径搜索从左上角到右下角来计算
# https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-by-leetcode-solution/
class Solution_offical:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        # 靠边的列 和 行
        for i in range(1, rows):     # 纵向叠加
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):  # 横向叠加
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # 中间元素叠加方法
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]

# 这里用的空间压缩方法，我还没有掌握，不会
# 很厉害
class Solution_offical1:
    def minPathSum(self, grid):
        dp = [float('inf')] * (len(grid[0])+1)
        dp[1] = 0
        for row in grid:
            for idx, num in enumerate(row):
                # 每次遍历时候，num和上面或左面的数字相加， dp[idx]代表左边加和，[idx+1]代表上边加和
                dp[idx + 1] = min(dp[idx], dp[idx + 1]) + num
        return dp[-1]


if __name__ == "__main__":
    grid = [
      [1,3,8],
      [1,3,0],
      [1,0,0]
    ]
    solu = Solution2()
    res = solu.minPathSum(grid)
    print(res)