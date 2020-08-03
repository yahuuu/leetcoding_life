# coding:utf-8
# Created data: 20200721


class Solution_nocut:
    def permute(self, nums):  # List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0: return []
        nums.sort()
        rt = []

        def helper(left, path, used):
            if len(path) == n:
                rt.append(path[:])
            for i in range(0, n):
                if used[i]: continue  # 用过的元素
                path.append(nums[i])
                used[i] = True
                helper(left+1, path, used)
                path.pop(-1)
                used[i] = False
        helper(0, [], [False for _ in range(len(nums))] )
        # [[1, 1, 2], [1, 2, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 1, 1]]
        return rt

# 接下来试下剪枝
class Solution:
    def permute(self, nums):  # List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0: return []
        nums.sort()
        rt = []

        def helper(left, path, used):
            if len(path) == n:
                rt.append(path[:])
                return
            for i in range(0, n):
                if used[i]: continue
                if i>0 and used[i-1] and nums[i-1] == nums[i]:  # 和上一位元素同，且上一个元素用过了，剪枝
                    continue
                path.append(nums[i])
                used[i] = True
                helper(left+1, path, used)
                path.pop(-1)
                used[i] = False
        helper(0, [], [False for _ in range(len(nums))] )
        # [[1, 1, 2], [1, 2, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 1, 1]]
        return rt

nums = [1, 2, 1]
s = Solution()
res = s.permute(nums)
print(res)