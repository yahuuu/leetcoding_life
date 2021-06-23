# -*- coding:utf-8 -*-
# Created data: 20200623
from typing import List


class Solution:
    def __init__(self):
        self.result = [1, 2, 1]

    def getRow(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return [1]
        elif numRows == 1:
            return [1, 1]
        elif numRows == 2:
            return [1, 2, 1]
        elif numRows > 2:
            self.helper(numRows)
            return self.result

    def helper(self, numRows):
        for i in range(3, numRows + 1):
            tmp2 = [1 for _ in range(i+1) ]
            for j in range(1, i):
                tmp2[j] = self.result[j - 1] + self.result[j]
            self.result = tmp2


if __name__ == "__main__":
    num = 7
    solu = Solution()
    ls = solu.generate(num)
    print(ls)
