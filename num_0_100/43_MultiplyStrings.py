# -*- coding:utf-8 -*-
# Created data: 20200726


# 思路： 123× 456 =
# 3*6 + 3*50 + 3*400 +
#          20*6 + 20*50 + 20*400 +
#                       100*6 + 100*50 + 100*400

class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        n1 = len(num1)-1
        n2 = len(num2)-1
        sum = 0
        for i in range(n1, -1, -1):
            n1_tmp = 10**(n1-i) * int(num1[i])
            for j in range(n2, -1, -1):
                # 2,1,0
                n2_tmp = 10**(n2-j) * int(num2[j])
                sum += n1_tmp*n2_tmp
        return str(sum)


s = Solution()
rt = s.multiply("123", "456")
print(rt)

# 另一种优化思路如下， 看到别人提交的时间复杂度不好，并不打算写
"""

                            1   2   3
                        乘  4   5   6
                    ————————————————————
                            6   12  18
                        5   10  15
                    4   8   12
                    ————————————————————
                    4   13  28  27  18
                    整理： c[i + 1] += c[i] / 10, c[i] %= 10, 从低位开始。
                    step 0: 4   13  28  27  18
                    step 1: 4   13  28  28  8
                    step 2: 4   13  30  8   8
                    step 3: 4   16  0   8   8
                    step 4: 5   6   0   8   8

# 思路来自：链接：https://leetcode-cn.com/problems/multiply-strings/solution/si-lu-qing-xi-by-lllllliuji-2/
"""
