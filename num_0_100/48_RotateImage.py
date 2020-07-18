# -*- coding:utf-8 -*-
# Created data:

# matrix =        [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]


# 原理很简单
# 对上边的矩阵先转置,然后换列, 2*O(N**2), 内存O(1)
class Solution1:
    def rotate(self, matrix): # List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return matrix
        r = len(matrix)  # i
        c = len(matrix[0])  # j
        for i in range(1, r):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(c//2):
            for j in range(r):
                matrix[j][i], matrix[j][r-1-i] = matrix[j][r-1-i], matrix[j][i]

        return matrix


# 原理和上边类似,但是旋转的轴是45°对称轴
# 时间复杂度: O(N**2)+O(1)
class Solution2(object):
    def rotate(self, matrix):  # List[List[int]]) -> None:
        if not matrix: return matrix
        r = len(matrix)  # i
        c = len(matrix[0])  # j
        for i in range(1, r):  # 1~3
            for j in range(r-1, r-1-i, -1):  # 3~1
                # 核心就是搞清坐标点的对应关系
                matrix[i][j], matrix[c-1-j][r-1-i] = \
                              matrix[c-1-j][r-1-i], matrix[i][j]
        # 这样时间复杂度到O(N)
        for i in range(r//2):
            matrix[i], matrix[r-1-i] = \
                       matrix[r-1-i], matrix[i]

        return matrix


# 方法三就是直接旋转移位
# 见图
# 同时控制好层次
# 难点还是在坐标, 好难计算
# 这个时间复杂度O(N/2 *N)
# 这道的时间复杂度应该是最好的,
# leetcode上有时击败97% 有时只有70%,也是醉了,休息
class Solution(object):
    def rotate(self, matrix):  # List[List[int]]) -> None:
        if not matrix: return matrix
        r = len(matrix)  # i
        c = len(matrix[0])  # j
        levels = c//2
        for level in range(levels):
            _tmp = c -2*level-1
            for i in range(0+level, _tmp+level, 1):
                matrix[level][i], matrix[i][c-1-level],\
                matrix[r-1-level][c-1-i], matrix[r-1-i][level] = \
                    matrix[r-1-i][level], \
                    matrix[level][i], matrix[i][c-1-level], \
                    matrix[r-1-level][c-1-i]

        return matrix

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]

s = Solution()
rt = s.rotate(matrix)
for i in rt:
    print(i)
