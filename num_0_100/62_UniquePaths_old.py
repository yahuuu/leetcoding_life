# -*- coding:utf-8 -*-
# Created data: 2020

# 递归真的很容易时间超出限制,没有通过
# 当然解法没有问题
# 我这个写法的思想是在递归树的底层叶子处来记录
class Solution_dfs1:
    def uniquePaths(self, m: int, n: int) -> int:
        self.num = 0
        def helper(m, n):
            if m==0 and n==0:  # 到目标的条件
                self.num += 1
                return  # 也是出口
            if m > 0:  #
                helper(m-1, n)
            if n > 0:  # 并列关系,递归树也可以往右走
                helper(m, n-1)
        helper(m-1, n-1)
        return self.num

# Todo: 接下来多练习递归
# 这是官方的解法,时间复杂度O(M*N),空间O(M*N)
class Solution_official:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        print(dp)
        #print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(len(dp)):
            print(dp[i])
        return dp[-1][-1]


# 这里的写法参考了上面官方思想,但是还是用递归,时间依然超限
# 这里递归的思想是计算好底层的路径种类,然后迭代,也是动态规划思想
class Solution_dfs2:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(m: int, n: int):
            # if (m==0 and n==1) or (m==1 and n==0):
            if m==0 or n==0:
                return 1
            elif m==1 and n==1:
                return 2
            else:
                return helper(m-1, n) + helper(m, n-1)
        return helper(m-1, n-1)


solu = Solution()
# res = solu.uniquePaths(3, 2)
res = solu.uniquePaths(7, 3)
print(res)
