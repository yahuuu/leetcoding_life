# coding:utf-8
# Code Date: 20200730


# 链接：https://leetcode-cn.com/problems/next-permutation/solution/ke-neng-shi-zui-jian-ji-de-pythonjie-da-by-luyao77/
# 这道题真不难，但是题意描述的很不清楚
# 举个例子：
# 比如 nums = [1,2,7,4,3,1]，下一个排列是什么？
# 我们找到第一个最大索引是 nums[1] = 2
# 再找到第二个最大索引是 nums[4] = 3
# 交换，nums = [1,3,7,4,2,1];
# 翻转，nums = [1,3,1,2,4,7]
# 链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-powcai/

class Solution:
    def nextPermutation(self, nums): # List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)-1, 0, -1):
        #     if nums[i] > nums[i-1]:
        #         nums[i:] = sorted(nums[i:])  # 数字右边从小到大排序
        #         for j in range(i, len(nums)):  # 从右边找比异常数大的元素，然后交换，打断
        #             if nums[j] > nums[i-1]:
        #                 nums[j], nums[i-1] = nums[i-1], nums[j]
        #                 break
        #         return
        # nums.sort()


nums = [3,1,2,3,5,4,1]
s = Solution()
s.nextPermutation(nums)
print(nums)
