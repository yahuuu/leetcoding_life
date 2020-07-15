# -*- coding:utf-8 -*-
# Created data: 20200709
import time


# 别人的解法, 公式
# def get_n(sum_result):
#     c = -2*sum_result
#     res = ((1-4*c)**(1/2)-1)/2
#     if res == int(res):
#         return int(res)
#     else:
#         return int(res)+1
#
# class Solution1:
#     @timers
#     def reachNumber(self, target: int) -> int:
#         target = -target if target<0 else target
#
#         n = get_n(target)
#         sum_result = (n**2+n)/2
#         if (sum_result-target)%2 == 0: # include sum_result==target
#             return n
#         elif n%2==0:
#             return n+1
#         return n+2


# 只考虑target为正,因为都是关于y轴对称
# 先一直往右走,累加和
# 如果当前的和比target大偶数,那么差/2的步数向左走就行,
# target = 7, 1+2+3+4 = 10, (10-7)/2=1.5,不合适的步
#             1+2+3+4+5= 15 ,(15-7)/2=4, 1+2+3-4+5=7 , ok
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        i = 0
        rt = 0
        while not (rt >= target and (rt-target)%2 == 0):
            i += 1
            rt += i
        return i


if __name__ == "__main__":
    import time
    target = 100
    s = Solution()
    print(s.reachNumber(target))
