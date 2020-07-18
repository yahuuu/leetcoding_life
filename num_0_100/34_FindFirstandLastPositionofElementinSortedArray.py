# -*- coding:utf-8 -*-
# Created data: 20200717

# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# 思路:二分法找目标点,找到了目标左右扩展范围搜索
# O(logN)+O(n)
# 内存和速度在榜单上都不占优势
class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        l = 0; r = len(nums)-1
        while l <= r: # and l>=0 and r<=len(nums)-1:
            if nums[l] > target or nums[r] < target:
                return [-1, -1]

            if nums[l] == target and nums[r] == target:
                return [l, r]
            mid_idx = (l+r)//2
            if nums[mid_idx] > target:
                r = mid_idx-1
            elif nums[mid_idx] < target:
                l = mid_idx+1
            else: # ==
                l = mid_idx; r = mid_idx
                while 1 and l >0 and r<len(nums)-1:
                    if nums[l-1]==target:
                       l -= 1
                    if nums[r+1]==target:
                       r += 1

                    if r>=len(nums)-1 or nums[l-1]!=target and nums[r+1]!=target:
                        break
                return [l, r]


# 这道题用hashmap思路最简单,
# 直接存起来所有的idx
# 但是建造树的时间O(1*N) + O(1)查询时间,并不占空间时间优势
class Solution(object):
    def searchRange(self, nums, target):
        if nums == []: return [-1, -1]
        hashmap = {}
        for idx, ele in enumerate(nums):
            # hashmap[ele] = hashmap.get(ele, []) + [idx]
            if hashmap.get(ele, None): hashmap[ele].append(idx)
            else: hashmap[ele] = [idx]

        tmp = hashmap.get(target)
        if not tmp:
            return [-1, -1]
        return [min(tmp), max(tmp)]


# nums = [0, 1, 1, 1, 2, 3, 5]
#         0  1  2  3  4  5  6
nums = [0,1,2,3,3,4,4,5,5,6,6,7,7,7,9,9,11,11,11,12,12,12,12]

s = Solution()
rt = s.searchRange(nums, 12)
print(rt)
