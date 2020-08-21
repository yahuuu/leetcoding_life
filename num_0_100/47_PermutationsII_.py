# -*- coding:utf-8 -*-
# Created data: 20200731


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = set()
        def permu(left):
            # if nums[left] in used:
            #     return
            if left == n:
                print(nums)
                rt.add(tuple(nums[:]))
                return
            for i in range(left, n):
                # used.add(nums[left])
                if left != i:
                    nums[left], nums[i] = nums[i], nums[left]
                permu(left+1)
                if left != i:
                    nums[left], nums[i] = nums[i], nums[left]
        n = len(nums)
        if n == 0: return []
        rt = set()
        permu(0)
        return [list(ls) for ls in rt]

nums = [1, 2, 3]
s = Solution()
rt = s.permuteUnique(nums)
print(rt)



