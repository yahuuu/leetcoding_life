# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 下午11:39
# @Author  : yahuuu
# @FileName: 168_excel-sheet-column-title.py
# @Software: PyCharm


# 题记这道题是进制的变种，我掉坑了，不是简单的进制
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # columnNumber -= 1
        chushu = 26
        ls = list()
        if columnNumber < 0:
            return ""
        if columnNumber  == 0:
            return "A"
        zhengshu = columnNumber
        while (zhengshu > 0):
            # 关键也就是这行对于26的处理
            zhengshu = columnNumber // chushu if columnNumber != 26 else 0
            yushu = columnNumber % chushu if columnNumber != 26 else 26
            if zhengshu:
                ls.append(chr(64 + yushu))
                columnNumber = zhengshu
        if yushu:
            ls.append(chr(64 + yushu))
        return "".join(ls[::-1])

# num = 2147483647
num = 52
solu = Solution()
result = solu.convertToTitle(num)
print(result)
