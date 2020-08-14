# coding:utf-8
# Code date: 20200

# 题意： 找和为最大的子串
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# #1 动态规划
# 思路：遍历, 动态规划， 公式 sum = max( sum[n-1] +ele, ele)
# 思路参考了： https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-cshi-xian-si-chong-jie-fa-bao-li-f/
# 公式解读： 第0到i个元素加和比第i个元素小，取i元素作为新的和，即子串新起点
# 遍历时候记录此时的最大值
# 这里内存是真省98% win， 时间百分比变化太大
class Solution_org(object):
    def maxSubArray(self, nums):
        if len(nums) == 1: return nums[0]
        acc = float("-inf")
        res = float("-inf")
        for i in nums:
            acc = max(acc+i, i)  # 是否丢弃之前的累加和
            res = max(res, acc)
        return res


class just_recursive(object):
    """只是写一个递归加和，并非结果"""
    def maxSubArray(self, nums):
        def helper(acc, i):
            if i >= n:
                return acc
            res = helper(acc + nums[i], i + 1)
            return res
        # for i in range()
        n = len(nums)
        # res = float("-inf")
        return helper(acc=0, i=0)


# 2. 递归来写上面的动态规划
# 我在这里只是把遍历改编成dfs
# 比较喜欢搞复杂的又得到正确结果的快感
# time win & mem win 都很惨, 哈
# 注意这颗递归树我不是在最深处比较局部值，在递归的每一层都要判断是否舍弃之前的加和，并找局部最大

class Solution2(object):
    def maxSubArray(self, nums):
        def helper(acc, i):
            nonlocal res
            if i >= n:
                return acc
            # 保留或者舍弃之前的加和
            # 如果扔掉， 当然此时只剩下当前元素num[i]
            sub_sum = max(acc + nums[i], nums[i])
            res = max(res, sub_sum)  # 局部最大和全局最大比较
            sub_sum = helper(sub_sum, i+1)
            return sub_sum   # U forget return again

        n = len(nums)
        res = float("-inf")
        helper(acc=0, i=0)
        return res


# 3. 分治, divide and conquer
# 思想： 最大值可能出现在左半部分，右半部分，跨中间点三种情况
# 分治是先把集合分成子集， 然后个个解决
# 参考了，链接中的c++解法：https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-cshi-xian-si-chong-jie-fa-bao-li-f/
class Solution(object):
    def maxSubArray(self, nums):

        def mid_sum(left, right):
            mid = (left+right) // 2
            left_sum = float("-inf")
            sub_sum = 0
            for i in range(mid, left-1, -1):  # 这里一定是倒叙， 为了从中间元素开始向左加和
                sub_sum += nums[i]
                left_sum = max(sub_sum, left_sum)  # 贪心找到左边的最大和
            right_sum = float("-inf")
            sub_sum = 0
            for i in range(mid+1, right+1, 1):
                sub_sum += nums[i]
                right_sum = max(sub_sum, right_sum)  # 贪心找到右边的最大和
            return left_sum+right_sum

        def divide_conquer(left, right):
            if left >= right:
                return nums[left]
            mid = (left + right)//2
            sum_l = divide_conquer(left, mid)
            sum_r = divide_conquer(mid+1, right)  # 所谓分治，先分解到底层再求解
            res = max(sum_l, sum_r)
            sum_mid = mid_sum(left, right)
            res = max(res, sum_mid)
            return res

        n = len(nums)
        return divide_conquer(0, n-1)


array = [-3, 2, 3, 4, -1, 2, 1, -1]
# array = [-2,1,-3,4,-1,2,1,-5,4]
# array= [-2, -1]  # 这个例子让我不再以0作为sum标准
# array=  [4, -1, 2, 1]
s = Solution()
res = s.maxSubArray(nums=array)
print(res)



