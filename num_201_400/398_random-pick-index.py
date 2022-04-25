#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/25
# @Author  : yahuuu

from typing import List
from collections import defaultdict

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for idx, ele in enumerate(nums):
            self.pos[ele].append(idx)
        print(self.pos)

    def pick(self, target: int) -> int:
        res = self.pos[target]
        return random.choice(res)


nums = [1, 2, 3, 3, 3]
solu = Solution(nums)
res = solu.pick(3)
print(res)