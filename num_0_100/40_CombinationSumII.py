#coding:utf-8
# Code Date: 20200722


# 40
# dfs+trackbacking
# 这道题查bug一次，提交AC但是速度不高
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # candidates.sort()
        rt = []
        n = len(candidates)
        def helper(left, ls, target):
            ls.append(candidates[left])
            target -= candidates[left]

            if target < 0:
                return
            if target == 0:
                if ls not in  rt:  # 排除重复元素 O(N)
                    rt.append(ls[:])  # solution

            # > 0
            for idx in range(left+1, n):
                helper(idx, ls, target)
                ls.pop(-1)  # traceback

        for i in range(len(candidates)):
            helper(i, [], target)
        return rt


# candidates = [1,2,3,4,5]
# target = 5
candidates = [10,1,2,7,6,1,5]
target = 8
s = Solution()
rt = s.combinationSum2(candidates, target)
print(rt)
