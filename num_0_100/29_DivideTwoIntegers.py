# coding:utf-8
# Code date: 20200803

# 思路：不能用乘法，取余和除法，那就减法。整除的结果意义是被除数中有多少个除数。
# 如果一次减一个除数，
# 时间会超限（2**31/1)。如果除数倍增，那么速度会极大提高。
# 这道题还要考虑32位整数的上限下限。以及除数、被除数的正负。
class Solution:
   def divide(self, dividend, divisor):
       """
       :type dividend: int
       :type divisor: int
       :rtype: int
       """
       MAX_INT = 2147483647
       MIN_INT = -MAX_INT -1
       positive = 1 if (dividend>0 and divisor>0) or (dividend<0 and divisor<0) else -1
       res = dividend
       num = 0
       dividend = abs(dividend)
       divisor = abs(divisor)
       while res >= divisor:
           dsor = divisor
           n = 1
           while dsor<<1 < res:
               dsor <<= 1
               n <<= 1
           res = res - dsor
           num += n
       num *= positive
       return max(min(num, MAX_INT), MIN_INT)


dividend, divisor = 100, -3
s = Solution()
res = s.divide(dividend, divisor)
print(res)


# from line_profiler import LineProfiler
# lp = LineProfiler()
# # lp.add_function(Solution.divide) # 被引用函数需要声明才显示细节
# lp_wrapper = lp(Solution().divide)  # 被显示的函数
# lp_wrapper(dividend, divisor)  # 参数传入
# lp.print_stats()  # 打印喽



a = 11; b = -34
def a1():
    x = a^b

def a2():
    if (a>0 and b>0) or (a<0 or b<0):
        pass

from timeit import timeit
t1 = timeit('a2', "from __main__ import a2", number=1000)
print(t1)
