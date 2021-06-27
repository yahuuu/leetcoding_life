# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 下午11:07
# @Author  : yahuuu
# @FileName: 504_base-7.py
# @Software: PyCharm


# 首先你得知道原理，余数是输出，取整更新被除数。
# 不用列表缓存快很多
class Solution:
    def convertToBase7(self, num: int) -> str:
        chushu = 7
        if num == 0: return "0"
        num1 = num if num > 0 else -1*num
        ans = 0
        ele = 1
        while(num1):
            yushu = num1 % chushu
            ans += yushu*ele
            num1 = num1 // chushu
            ele *= 10
        if num < 0:
            ans *= -1
        return str(ans)


# 列表缓存
class Solution1:
    def convertToBase7(self, num: int) -> str:
        chushu = 7
        if num == 0: return "0"
        num1 = num if num > 0 else -1*num
        ls = []
        while(num1):
            ls.append(str(num1 % chushu))
            num1 = num1 // chushu
        if num < 0:
            ls.append("-")
        return "".join(ls[::-1])


solu = Solution()
ret = solu.convertToBase7(-7)
print(ret)
