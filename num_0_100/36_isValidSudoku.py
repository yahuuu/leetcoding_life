# coding:utf-8
# Code date: 20200810

# 题目 ：
# https://leetcode-cn.com/problems/valid-sudoku/solution/you-xiao-de-shu-du-by-leetcode/
# 官方的解法，思路就是查询元素，存起来，重复返回False
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3  # 核心就一行代码

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True

# TODO1： 现在你知道题意了，明天写个自己的解法吧
# 用嵌套列表能省下存放键指针的内存, 索引查询速度也不差

# time win 98.9%
class Solution1(object):
    def isValidSudoku(self, board):
        block = [set() for _ in range(9)]
        row =   [set() for _ in range(9)]
        col =   [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                ele = board[r][c]
                if ele == ".":
                    continue
                block_idx = (r//3)*3 + c//3
                if ele in row[r] or ele in col[c] or ele in block[block_idx]:
                    return False
                row[r].add(ele)
                col[c].add(ele)
                block[block_idx].add(ele)
        return True


board = [
    ["1", ".", ".", ".", ".", ".", ".", ".", "."],
    ["2", ".", ".", ".", ".", ".", ".", ".", "."],
    ["1", ".", ".", "2", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "3", ".", ".", ".", ".", ".", "."],
    [".", "4", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]
s = Solution1()
res = s.isValidSudoku(board)
print(res)



