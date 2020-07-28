# -*- coding:utf-8 -*-
# Created data: 2020

# NO AC: 217 / 282 个通过测试用例
# 剪枝不够导致时间超时?
class Solution1(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(left, ls, sum):
            if len(ls) < 2 and n-1 -left < 2: return  # cut
            if sum == target and len(ls) == 4:
                rt.add(tuple(ls[:]))
            if sum > target: return  # cut
            for j in range(left+1, n):
                sum += nums[j]
                ls.append(nums[j])
                helper(j, ls, sum)
                sum -= nums[j]
                ls.pop(-1)
        if not nums:
            return []
        rt = set()
        nums = sorted(nums)
        n = len(nums)
        for i in range(n-3):
            helper(i, [nums[i]], nums[i])
        return [list(ele) for ele in rt]

# 时间复杂度不行
# O(N**4)
class Solution2(object):
    def fourSum(self, nums, target):
        nums.sort()
        if len(nums) <= 3: return []
        i, j, k, l= 0, 1, 2, 3
        n = len(nums)
        rt = set()
        for i in range(0, n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for l in range(k+1, n):
                        tmp = (nums[i], nums[j], nums[k], nums[l])
                        if sum(tmp) > target: break
                        elif sum(tmp) == target:
                            rt.add(tmp)
        return [list(ele) for ele in rt]

# AC but exceed 62% in time
# O(N**3)
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        if len(nums) <= 3: return []
        i, j, k, l= 0, 1, 2, 3
        n = len(nums)
        rt = set()
        for i in range(0, n-3):
            if (nums[i] + 3*nums[i+1] > target) or (nums[i]+3*nums[-1]<target):
                continue
            for j in range(i+1, n-2):
                k, l = j+1, n-1
                while k < l:
                    tmp = (nums[i], nums[j], nums[k], nums[l])
                    if k >= l: break
                    if sum(tmp) > target:
                        l -= 1
                    elif sum(tmp) == target:
                        l -= 1
                        k += 1
                        rt.add(tmp)
                    elif sum(tmp) < target:
                        k += 1

        return [list(ele) for ele in rt]

# nums = [-2, -1, 0, 0, 1, 2] # 0,1,2,3,4,5,6]
# target = 1
nums = \
[-483,-464,-417,-372,-315,-303,-283,-282,-267,-265,-262,-256,-254,-248,-247,-245,-200,-200,-194,-192,-183,-155,-83,-69,-59,-44,-42,-40,-24,-18,-14,-11,0,4,10,28,38,59,87,126,135,147,151,152,162,187,211,214,218,248,274,282,287,288,329,331,338,364,366,384,405,476,477,488]
target = 1563
#               i j k l
s = Solution()
rt = s.fourSum(nums, target)
import sys
sys.stdout.write(str(rt))
