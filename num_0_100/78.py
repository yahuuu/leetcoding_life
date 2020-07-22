#coding:utf-8

# 78
# 下面两种方法都是dfs+backcall
# 只不过在第一个数值的处理上不同
# 回溯要记得恢复上一次的状态
class Solution(object):
    def search(self, nums):
        rt = [[]]
        n = len(nums)
        def helper(left, ls):
            if left >= n: return
            ls.append(nums[left])
            rt.append(ls.copy())
            for idx in range(left+1, n):
                helper(idx, ls)
                ls.pop(-1)

        for i in range(n):
            helper(i, [])
        return rt


class Solution2(object):
    def search(self, nums):
        rt = [[]]
        n = len(nums)
        def helper(left, ls):
            if left >= n: return
            rt.append(ls.copy())
            for idx in range(left + 1, n):
                ls.append(nums[idx])
                helper(idx, ls)
                ls.pop(-1)

        for i in range(n):
            helper(i, [nums[i]])
        return rt


nums = [1,2,3]
s = Solution2()
rt = s.search(nums)
print(rt)
