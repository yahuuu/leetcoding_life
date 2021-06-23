# -*- coding:utf-8 -*-
# Created data: 20200623
from typing import List


class Solution:
    def __init__(self):
        self.ls1 = [[1], [1, 1]]
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <=0:
            return []
        elif numRows ==2:
            return self.ls1
        elif numRows == 1:
            return [[1]]
        elif numRows > 2:
            self.helper(numRows)
            return self.ls1


    def helper(self, numRows):
        for i in range(3, numRows+1):
            tmp = [1]
            for j in range(i-2):
                tmp.append(self.ls1[i-2][0+j] + self.ls1[i-2][1+j])
            tmp.append(1)
            self.ls1.append(tmp)

if __name__ == "__main__":
    num = 15
    solu = Solution()
    ls = solu.generate(num)
    for i in range(num):
        print("{:^100s}".format(str(ls[i])))





