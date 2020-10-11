# -*- coding:utf-8 -*-
# Created data: 20201011

from typing import List

# ONCE AC
# 思路和１２１类似, 这里需要维护栈
# time: O(N) + mem: O(N)
# 遍历股价
# 当栈空，元素入栈
# 栈不为空，元素>=栈顶，入栈
# 否则，元素<栈顶，计算此时的获利:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        stack = []
        for price in prices:
            if not stack:
                stack.append(price)
                continue
            if price >= stack[-1]:
                stack.append(price) # 股价升,不卖
            else: # if stack[0] <= price <= stack[-1]:
                if len(stack) > 1:
                    res += stack[-1]-stack[0]  #卖，增加当前栈的获利
                stack = [price]

        if len(stack) > 1: # 最后清算栈中获利
            res += stack[-1] - stack[0]
        return res


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 1, 4]
    solu = Solution()
    res = solu.maxProfit(prices)
    print(res)
