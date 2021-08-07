# -*- coding: utf-8 -*-
# @Time    : 2021/8/4 下午10:15
# @Author  : yahuuu
# @FileName: 128_longest-consecutive-sequence.py
# @Software: PyCharm


from collections import defaultdict
from typing import List
# 核心思想：是并查集(查找根节点+树合并），计数的方法是在合并树的时候，新的根节点+=老的节点的计数
# 并查集，可以不用排序就找到最大连续元素的数量，其实是树的构建过程，根用来统计总数，
# 还需要对树进行剪枝。
class Solution:
    def find(self, ele):
        if self.parents[ele] == None:
            return ele
        while self.parents[ele] != None:
            ele = self.parents[ele]
        return ele

    def union(self, i, j):
        rootx = self.find(i)
        # 只有一个数在，查个数并返回
        if j not in self.num:
            return self.cnt[rootx]
        rooty = self.find(j)
        if rootx == rooty:
            return self.cnt[rooty]
        else:
            # 大的元素上统计个数
            self.cnt[rooty] += self.cnt[rootx]
            self.parents[rootx] = rooty
            return self.cnt[rooty]

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        self.num = set(nums)
        self.parents = defaultdict(lambda: None)
        self.cnt = defaultdict(lambda: 1)
        cnt = 1
        for ele in self.num:
           cnt = max(cnt, self.union(ele, ele + 1))
        return cnt


if __name__ == '__main__':
    ls = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
    solu = Solution()
    res = solu.longestConsecutive(ls)
    print(res)

