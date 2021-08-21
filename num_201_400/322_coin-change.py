# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 下午11:31
# @Author  : yahuuu
# @FileName: 322_coin-change.py
# @Software: PyCharm

from typing import List

# 动态规划的难点就是想明白转移方程怎么写
# F(amount) = min(F(amout - coin[i])) + 1
# 枚举任何一种可能的组合
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            # 把多循环的放内层
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


# 我的解法是贪心： 枚举是从最大的硬币开始，但是数量不一定最少。比如
#　找零１４元，coins　是　[10, 7, 1]
# 我的解法只能返回　１０＋１＊４的组合,
# 这题明显不是在考察贪心
class Solution_my(object):
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        for idx in range(len(coins), 0, -1):
            _coins = coins[: idx]
            res = 0
            yuer = amount
            coins_type = len(_coins)
            while yuer > 0 and coins_type > 0:
                coins_type -= 1
                num = yuer // _coins[coins_type]
                yuer %= _coins[coins_type]
                if num > 0:
                    res += num
            if yuer == 0 and res > 0:
                return res
        return -1


if __name__ == '__main__':
    coins = [1, 7, 10]
    amount = 14
    solu = Solution()
    res = solu.coinChange(coins, amount)
    print(res)
