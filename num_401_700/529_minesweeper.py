# -*- coding: utf-8 -*-
# @Time    : 2021/8/8 上午11:09
# @Author  : yahuuu
# @FileName: 529_minesweeper.py
# @Software: PyCharm


from typing import List

# 好久没写DFS了，手生，记得原理

class Solution:
    def check_valid(self, x, y):
        if x >= self.limitx or x < 0 or y < 0 or y >= self.limity:
            return False
        return True

    def cout_mines(self, x, y) -> int:
        if not self.check_valid(x, y):
            return -1
        if self.old_path[x][y] == -1:
            return -1
        res = 0
        for xx, yy in self.ls:
            if not self.check_valid(x+xx, y+yy):
                continue
            if self.board[x + xx][y + yy] == "M":
                res += 1
        self.old_path[x][y] = -1
        return res

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.limitx = len(board)
        self.limity = len(board[0])
        x, y = click[0], click[1]
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        # 我开始没有加路径状态的记录，　-1 状态为走过，　０是全新
        # 　这样会导致递归栈溢出，因为可能路径会来回踱步
        self.old_path = list([0] * self.limity for i in range(self.limitx))
        self.ls = [[-1, 0], [-1, 1], [0, 1], [1, 1],
                   [1, 0], [1, -1], [0, -1], [-1, -1]]
        self.board = board
        self.update_status(x, y)
        return self.board

    def update_status(self, x, y):
        res = self.cout_mines(x, y)
        if res > 0:
            self.board[x][y] = str(res)
            return
        if res == 0:
            self.board[x][y] = "B"
            for xx, yy in self.ls:
                self.update_status(x + xx, y + yy)


if __name__ == '__main__':
    board = \
    [["E", "E", "E", "E", "E", "E", "E", "E"],
     ["E", "E", "E", "E", "E", "E", "E", "M"],
     ["E", "E", "M", "E", "E", "E", "E", "E"],
     ["M", "E", "E", "E", "E", "E", "E", "E"],
     ["E", "E", "E", "E", "E", "E", "E", "E"],
     ["E", "E", "E", "E", "E", "E", "E", "E"],
     ["E", "E", "E", "E", "E", "E", "E", "E"],
     ["E", "E", "M", "M", "E", "E", "E", "E"]]
    Click = [0, 0]
    solu = Solution()
    res = solu.updateBoard(board, Click)
    supposed = \
        [["B", "B", "B", "B", "B", "B", "1", "E"], ["B", "1", "1", "1", "B", "B", "1", "M"],
         ["1", "2", "M", "1", "B", "B", "1", "1"], ["M", "2", "1", "1", "B", "B", "B", "B"],
         ["1", "1", "B", "B", "B", "B", "B", "B"], ["B", "B", "B", "B", "B", "B", "B", "B"],
         ["B", "1", "2", "2", "1", "B", "B", "B"], ["B", "1", "M", "M", "1", "B", "B", "B"]]
    for i in range(len(supposed)):
        print(res[i], end=" ")
        print(supposed[i], end="\n")
