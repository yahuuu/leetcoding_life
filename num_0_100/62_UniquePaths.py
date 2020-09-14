# coding:utf-8
# Code date: 20200901


# 递归的实现2.另一种递归实现方法是在递归的底层计数
# 时间会超限
# 我这个写法的思想是在递归树的底层叶子处来记录路径的和
class Solution_recurion1:
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
# 时间和官方解法基本相同
# 优化很成功
class Solution_recursion2:
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
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # print(dp)
        return dp[-1][-1]
# [[1, 1, 1],
#  [1, 2, 3],
#  [1, 3, 6],
#  [1, 4, 10]]
class Solution_org1:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        # print(cur)
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        # print(cur)
        return cur[-1]

# 这里的写法参考了上面官方思想,但是还是用递归,时间依然超限
# 这里递归的思想是计算好底层的路径种类,然后迭代,也是动态规划思想
class Solution_recursion3:
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


if __name__ == "__main__":
    m, n = 4, 3
    # solu = Solution_org1()
    solu = Solution_recursion3()
    res = solu.uniquePaths(m, n)
    print(res)

    # from line_profiler import LineProfiler
    # lp = LineProfiler()
    # # lp.add_function(Solution1.)  # 被引用函数需要声明才显示细节
    # lp_wrapper = lp(Solution2().uniquePaths)  # 被显示的函数
    # # lp_wrapper = lp(Solution_org().uniquePaths)  # 被显示的函数
    # lp_wrapper(m, n)  # 参数传入
    # lp.print_stats()  # 打印喽
