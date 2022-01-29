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


class Solution1:
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


"""
最小堆大概思路， 第k个最小就是堆中第k次出堆的元素，
入堆的元素是：(和， points)
每次循环中，先弹出最小元素，
从最小元素的下标分别向右 移动一次，
大概现象是每次弹出的元素向右扩展，

"""

import heapq as hq


class Solution:
    def __init__(self):
        self.ls = list()
        self.mat = None
        self.used = set()

    def return_va_point(self, points):
        val = sum([self.mat[i][points[i]] for i in range(self.row)])
        return val

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        self.mat = mat
        self.row = row = len(mat)
        col = len(mat[0])
        points = [0] * row
        val = 0
        for i in range(self.row):
            val += self.mat[i][0]
        # val = sum([self.mat[i][points[i]] for i in range(self.row)])

        hq.heappush(self.ls, (val, points))
        self.used.add(tuple(points))
        for _ in range(k - 1):
            val, points = hq.heappop(self.ls)
            # 每行当前point列往前走一步
            for j in range(row):
                new_points = points.copy()
                new_points[j] += 1
                if new_points[j] > col - 1:  # 超过col
                    continue
                if tuple(new_points) in self.used:
                    continue
                self.used.add(tuple(new_points))
                # val = sum([self.mat[n][new_points[n]] for n in range(self.row)])  #  事实证明这行特别费时间
                # val = sum(list(self.mat[i][new_points[i]] for i in range(self.row))) # 生成器也不快
                new_val = val - mat[j][points[j]] + mat[j][new_points[j]]

                hq.heappush(self.ls, (new_val, new_points))
        return hq.heappop(self.ls)[0]


import heapq


class Solutionk:
    def kthSmallest(self, mat, k: int) -> int:
        m, n = len(mat), len(mat[0])
        # 初始化指针
        pointers = [0] * m
        # 初始化heap
        heap = []
        curr_sum = 0
        for i in range(m):
            curr_sum += mat[i][0]
        heapq.heappush(heap, [curr_sum, tuple(pointers)])
        # 初始化seen
        seen = set()
        seen.add(tuple(pointers))
        # 执行k次
        for _ in range(k):
            # 从堆中pop出curr_sum(最小数组和)和pointers(指针数组)
            curr_sum, pointers = heapq.heappop(heap)
            # 每个指针轮流后移一位，将new_sum(新的数组和)和new_pointers(新的指针数组)push入堆
            for i, j in enumerate(pointers):
                if j < n - 1:
                    new_pointers = list(pointers)
                    new_pointers[i] = j + 1
                    new_pointers = tuple(new_pointers)
                    if new_pointers not in seen:
                        new_sum = curr_sum + mat[i][j + 1] - mat[i][j]
                        heapq.heappush(heap, [new_sum, new_pointers])
                        seen.add(new_pointers)
        return curr_sum


if __name__ == '__main__':
    mat = [[1, 1, 10], [2, 2, 9]]
    k = 7
    solu = Solution()
    res = solu.kthSmallest(mat, k)
    print(res)
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    # ♠2
    # from line_profiler import LineProfiler
    # lp = LineProfiler()
    # lp.add_function(Solution.kthSmallest)  # 被引用函数需要声明才显示细节
    # lp_wrapper = lp(Solution().kthSmallest)  # 被显示的函数
    # lp_wrapper(mat, k)  # 参数传入
    # lp.print_stats()  # 打印喽
