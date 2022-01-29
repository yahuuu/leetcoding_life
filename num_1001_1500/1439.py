# 这个方法和纯粹的暴力递归, 一样超时
# 得剪枝
import heapq as hq
from typing import List


class Solution2:
    def __init__(self):
        self.ls = list()
        self.r = 0
        self.c = 0
        self.k = 0
        self.mat = None

    def helper(self, sum, row_idx):
        if len(self.ls) > self.k:
            hq.heappop(self.ls)
        if row_idx >= self.r:
            hq.heappush(self.ls, -sum)
            return
        for c in range(self.c):
            sum += self.mat[row_idx][c]
            row_idx += 1
            self.helper(sum, row_idx)
            row_idx -= 1
            sum -= self.mat[row_idx][c]

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        self.k = k
        self.r = len(mat)
        self.c = len(mat[0])
        self.mat = mat
        self.helper(0, 0)
        self.ls.sort(reverse=True)
        return -self.ls[k - 1]


# 就算是用单调队列优化也是一样在第28个用例超限，
# 坑真深，得优化剪枝
from collections import deque


class Solution3:
    def __init__(self):
        # 单调队列, 递减， 优先队列的元素有优先级
        self.deq = deque()
        self.r = 0
        self.c = 0
        self.k = 0
        self.mat = None

    def helper(self, sum, row_idx):
        while len(self.deq) > self.k:
            self.deq.pop()
        if row_idx >= self.r:
            ls = []
            while self.deq and self.deq[-1] > sum:
                ls.append(self.deq.pop())
            self.deq.append(sum)
            while ls:
                self.deq.append(ls.pop(-1))
            return
        for c in range(self.c):
            sum += self.mat[row_idx][c]
            row_idx += 1
            self.helper(sum, row_idx)
            row_idx -= 1
            sum -= self.mat[row_idx][c]

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        self.k = k
        self.r = len(mat)
        self.c = len(mat[0])
        self.mat = mat
        self.helper(0, 0)
        # self.ls.sort(reverse=False)
        return self.deq[k - 1]


"""暴力终于通过了，
原理基本是bfs，一行行处理，但是要剪枝，每次只取tmp前k个元素,
多余扔掉，这么剪枝。
回溯法不适合这道题吧。
"""


class Solution:
    def __init__(self):
        self.deq = list()

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        row = len(mat)
        col = len(mat[0])
        self.deq.extend(mat[0])
        for r in range(1, row):
            tmp = list()
            for c in range(col):
                for ele in self.deq:
                    tmp.append(mat[r][c] + ele)
            tmp = sorted(tmp, reverse=False)
            self.deq = tmp[:k]
        return self.deq[k - 1]
