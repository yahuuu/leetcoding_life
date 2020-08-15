# coding:utf-8
# Code date: 20200815

class Solution:
    dict = {}
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        tmp = self.dict.get(n, None)
        if tmp != None:
            return tmp
        else:
            rlt = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.dict[n] = rlt
            return rlt


s = Solution()
res = s.climbStairs(4)
print(res)