# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 下午9:47
# @Author  : yahuuu
# @FileName: unionVector.py
# @Software: PyCharm

class existCircle():
    def find_parents(self, idx):
        if (self.ls[idx] == -1):
            return idx
        while (self.ls[idx] != -1):
            idx = self.ls[idx]
        return idx

    def union_vector(self, x, y) -> bool:
        rootx = self.find_parents(x)
        rooty = self.find_parents(y)
        if (rootx == rooty):
            return True
        self.ls[rootx] = rooty
        return False

    def find(self, num, edges):
        self.ls = [-1] * num
        for x, y in edges:
            if self.union_vector(x, y):
                return True
        return False


if __name__ == "__main__":
    edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 4]]  # 边集
    num = 5
    tool = existCircle()
    res = tool.find(num, edges)
    print(res)


