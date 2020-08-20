# coding:utf-8
# Code date: 20200820


from typing import List
# 思路很简单，就是顺时针取元素
# 关键点就是控制好元素的坐标边界点，并且要注意层次关系
# 空间复杂度O(1)除了必须输出的数组， 时间复杂度O(M*N)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        if len(matrix) == 1:
            return matrix[0]
        import math
        col = len(matrix[0])-1
        row = len(matrix)-1
        res = []
        levels = min(math.ceil((row+1)/2), math.ceil((col+1)/2))
        for level in range(levels):
            # 第一行
            for i in range(0+level, col+1 -level, 1):
                res.append(matrix[0+level][i])
            # 第N-1列, 掐头去尾
            for i in range(level+1, row-level, 1):
                res.append(matrix[i][col-level])
            # 第N-1 行
            if 0+level < row-level:  # 防止奇数行时，第n-1行被重复取
                for i in range(col-level, -1+level, -1):
                    res.append(matrix[row-level][i])
            # 第0列, 掐头去尾
            if 0+level < col-level:  # 防止奇数列时，第0列被重复取
                for i in range(row-1-level, 0+level, -1):   # 只控制行 坐标
                    res.append(matrix[i][0+level]) # 列坐标在循环里
        return res

matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
# matrix = [
#   [1, 2, 3 ],
#   [5, 6, 7 ],
#   [9, 10, 11],
#   [13,14,15 ]
# ]
s = Solution()
res = s.spiralOrder(matrix)
print(res)

#  [ 1, 2, 3 , 3 ],
#  [ 4, 5, 6 , 6 ],
#  [ 7, 8, 9 , 9 ],
#  [ 1, 2, 3 , 3 ],

# Input:
# 00 01 02 0n-1
# 1n-1  2n-1 n-1n-1
# n-1n-2 ...  n-10
# n-10 n-20     00
# 11 12

# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Input:
# [
# ]
# Output: [1,2,3,6,9,8,7,4,5]