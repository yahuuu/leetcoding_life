# -*- coding:utf-8 -*-
# Created data: 2020905


from typing import List
# time exceed: 87%
# tracebacking 有阵子没练习了,生疏了
# 只记得思想了,写起来费劲
class Solution_recursion:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(path, idx, layers):
            if (n-idx+1) < k-layers:  # pruning # 当前剩余元素不够用了
                return
            if layers==k:
                res.append(path[:])
                return
            for i in range(idx, n+1):  # 横向扩展递归树
                path.append(i)
                layers += 1
                helper(path, i+1, layers)  # one step forward
                layers -= 1  # backtracking
                path.pop(-1)
        helper(path=[], idx=1, layers=0)
        return res


if __name__ == "__main__":
    # 1, 2, 3, 4
    # k = 2
    # 1, 2, 3, 4
    # k = 3
    # 123  134  234
    #  -4   -
    n, k = 4, 3
    solu = Solution_recursion()
    res = solu.combine(n, k)
    print(res)