# -*- coding:utf-8 -*-
# Created data: 20201011


from typing import List

# 时间复杂度超限制, java可以通过
# 我的解法：暴力遍历
# O(N**2)
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] < prices[i]:
                    continue
                res = max(prices[j]-prices[i] , res)
        return res

# 这是官方的解法二
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/
# 思路：出现股价差的时候一定是用到了历史曲线中的最小值,
# 所以遍历时候记录当前最小值，之后的股价和临时最小值比较差，若大更新到res中即可
# time: O(N) + mem: O(1)
# 不需要维护栈空间
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float("inf")
        res = 0
        for price in prices:
            res = max(price-minp, res)
            minp = min(minp, price)
        return res

# 栈
# 思路：出现股价差的时候一定是用到了历史曲线中的最小值,
# 我在精选题解(栈＋哨兵)基础上去掉了哨兵：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/c-li-yong-shao-bing-wei-hu-yi-ge-dan-diao-zhan-tu-/
# 并且改进了不断弹元素的思路：
# 栈只入栈不弹出, 会省掉弹出元素的时间
#　思路：　如果栈当前为空，那么直接入栈，
# 如果当前元素比栈顶元素大那么入栈，　比较栈顶栈底元素并更新res
# 如果当前元素在栈底元素和栈顶元素之间, 那么当前元素抛弃
# 如果当前元素比栈底元素小，那么栈直接删除，当前元素作为栈中元素
# time: O(N) + mem: O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        stack = []
        for price in prices:
            if not stack:
                stack.append(price)
                continue
            if price > stack[-1]:
                stack.append(price)
                res = max(stack[-1]-stack[0], res)
            elif stack[0] <= price <= stack[-1]:
                continue
            elif stack[0] > price:
                stack = [price]
        return res


if __name__ == "__main__":
    prices = [1, 5, 3, 6, 4, 9]
    # prices = [7, 6, 4, 3, 1]
    solu = Solution()
    res = solu.maxProfit(prices)
    print(res)
