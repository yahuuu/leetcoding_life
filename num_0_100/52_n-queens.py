import copy
from typing import List

"""
n皇后写起来也不是很难，
还是那句话，想清楚逻辑，否则debug很费劲。
这道题看到可以用集合来做valid部分的优化。
"""
class Solution:
    def __init__(self):
        self.res = list()
        self.n = None
    def helper(self, tmp, idx, valid_num):
        if valid_num == self.n:
            # 注意多层嵌套list这么copy，否则还是浅层copy
            self.res.append(copy.deepcopy(tmp))
            return
        for i in range(0, self.n):
                if self.is_valid(tmp, idx, i):
                    tmp[idx][i] = "Q"
                    self.helper(tmp, idx+1, valid_num+1)
                    tmp[idx][i] = "."
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        tmp = [["." for j in range(n)] for i in range(n)]
        self.helper(tmp, 0, 0)
        return self.convert()

    def is_valid(self, tmp, i, j):
        # 纵向
        for c in range(0, i):
            if tmp[c][j] == "Q":
                return False
        # 左斜角
        c = j - 1
        for r in range(i-1, -1, -1):
            if c < 0: break
            if tmp[r][c] == "Q":
                return False
            c -= 1
        # 右斜角
        c = j + 1
        for r in range(i-1, -1, -1):
            # 控制边界
            if c >=self.n: break
            if tmp[r][c] == "Q":
                return False
            c += 1
        return True

    def convert(self):
        result = list()
        for i in self.res:
            result.append(["".join(j) for j in i])
        return result


if __name__ == '__main__':
    solu = Solution()
    res = solu.solveNQueens(4)
    print(res)
