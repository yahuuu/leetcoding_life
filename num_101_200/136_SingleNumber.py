# -*- coding:utf-8 -*-
# Created data: 20201002


from typing import List


# 这个题目考察位运算，位运算
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(0, len(nums)):
            res ^= nums[i]
        return res


if __name__ == "__main__":
    nums = [2, 2, 3, 3, 4 ]
    solu = Solution()
    res = solu.singleNumber(nums)
    print(res)


# python的位运算
# 位与，　或，　异或运算
# &      |      ^
# 异或运算：　满足交换律，相同数字异或运算的结果是０