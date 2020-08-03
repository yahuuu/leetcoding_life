# -*- coding:utf-8 -*-
# Created data: 20200709

# https://leetcode-cn.com/problems/binary-search/
# 第一遍写的时候忘了写返回, return helper(mid+1, end) 那里一定记得取回返回值

class Solution:
    def search(self, nums, target): #: List[int], target: int) -> int:
        if not nums: return -1
        def helper(start, end):
            if start > end: return -1
            mid = (start+end) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target:
                return helper(mid+1, end)
            else: # nums[mid] > target:
                return helper(start, mid-1)

        return helper(0, len(nums)-1)


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 8
    s = Solution()
    rt = s.search(nums, target)
    print(rt)