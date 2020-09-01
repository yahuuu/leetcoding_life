# coding:utf-8
# Code date: 20200901


# 另一种递归实现方法是在递归的底层计数
# 时间会超限
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        self.num = 0
        def helper(m, n):
            if m==0 and n==0:  # 符合的条件
                self.num += 1
            elif m<0 or n<0:  # 出栈条件
                return
            else:
                helper(m-1, n)
                helper(m, n-1)
        helper(m-1, n-1)
        return self.num


# 递归实现方法1, 这种思路是统计递归树的分裂次数
# 这里做了时间优化，否则也会时间超限
# time win 97%
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        dic = {}
        def helper(m, n):
            res = dic.get((m, n), None) or dic.get((n, m), None)
            if res != None:
                return res
            else:
                if m==0 or n==0:
                    return 1
                else:
                    res = helper(m, n-1) + helper(m-1, n)
                    dic[(m, n)] = res
                    return res
        return helper(m-1, n-1)


# 官方的思路是迭代, 动态规划
# 空间复杂度O(M*N)
class Solution_org:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print(dp)
        return dp[-1][-1]
# [[1, 1, 1],
#  [1, 2, 3],
#  [1, 3, 6],
#  [1, 4, 10]]
class Solution_org1:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        print(cur)
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        print(cur)
        return cur[-1]


if __name__ == "__main__":
    m, n = 4, 3
    solu = Solution_org1()
    # solu = Solution1()
    res = solu.uniquePaths(m, n)
    print(res)
