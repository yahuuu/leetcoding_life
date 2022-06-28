#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28
# @Author  : yahuuu

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
            print(n)
        return n == 1

if __name__ == '__main__':
    solu = Solution()
    res = solu.isHappy(2)
    print(res)

