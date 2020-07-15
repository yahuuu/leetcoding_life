#coding:utf-8
#Code Date: 20200715
# 这道题直接用二分法可以搞定，
# 处理好边界值的情况,就ok

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        def helper(start, end):
            if start > end: return max(start, end), False
            # 把下面的注释打开就可以超越77%， 我也是醉了
            # 列表元素索引不是O(1)吗， 这么耗时？
            # if start == end:
            #     if nums[start] > target:
            #         return start, False
            #     elif nums[start] < target:
            #         return start+1, False
            #     else:
            #         return start, True
            mid = (start+end)//2
            if nums[mid] == target:
                return mid, True
            elif nums[mid] < target:
                return helper(mid+1, end)
            else:
                return helper(start, mid-1)

        end = len(nums)-1
        return helper(0, end)[0]


nums =[0,1,2,3,4,5,6]
target = -2

s = Solution()
rt = s.searchInsert(nums, target)
print(rt)