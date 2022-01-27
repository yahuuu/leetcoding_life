from typing import List
from collections import deque

"""单调队列的实现方法，On
官方题解是存放下标，这样内存省一点，我是存放（下标，数值）的元组"""


class Solution:
    def __init__(self):
        self.ls = deque()
        self.res = list()

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        for i in range(k):
            self.inMonotonicQueue(nums[i], i)
        self.res.append(self.ls[0][0])
        # self.ls.popleft()
        for j in range(k, len(nums)):
            # 如果是个递减数组，第一个元素的过期时间，用idx控制, 往后走了k步，可能会发生最大值失效问题。
            if (j - self.ls[0][1]) == k:
                self.ls.popleft()
            self.inMonotonicQueue(nums[j], j)
            self.res.append(self.ls[0][0])
        return self.res

    def inMonotonicQueue(self, param, idx):
        # 维护一个单调队列，递减
        while (self.ls and self.ls[-1][0] < param):
            self.ls.pop()
        self.ls.append((param, idx))


"""最小堆, python 默认最小堆，入堆负数可以反着用,
nlogn = n*堆化的时间复杂度logn
晚上刷题脑子挺累了。
"""
import heapq as hq


class Solution1(object):
    def __init__(self):
        self.ls = list()
        self.res = []

    def maxSlidingWindow(self, nums, k):
        for i in range(k):
            self.ls.append((-nums[i], i))
        hq.heapify(self.ls)
        self.res.append(-self.ls[0][0])

        for i in range(k, len(nums)):
            # method 1
            # self.ls.append((-nums[i], i))
            # hq.heapify(self.ls)  # 应该是每次都需要堆化
            # method 2
            hq.heappush(self.ls, (-nums[i], i))
            # 1和2的区别主要是 时间复杂度，
            # 1 是nlogn， 2是logn
            while self.ls and (i - self.ls[0][1]) >= k:
                hq.heappop(self.ls)
            self.res.append(-self.ls[0][0])
        return self.res

#
# if __name__ == "__main__":
#     nums = [1, 3, 1, 2, 0, 5]
#     k = 3
#     solu = Solution()
#     res = solu.maxSlidingWindow(nums, k)
#     print(res)
