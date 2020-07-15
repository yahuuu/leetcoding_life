# -*- coding:utf-8 -*-
# Created data: 20200715

# 思路来自: https://leetcode-cn.com/problems/unique-binary-search-trees/solution/shou-hua-tu-jie-san-chong-jie-fa-dp-di-gui-ji-yi-h/
# 用 i 个节点构建子树，除去根节点，剩下 i-1 个节点构建左右子树，
# 左子树分配了 0 个，那么右子树相应的分配到 i-1 个，以此类推
# n = 2
#        1     1
#      /         \
#    2             2
#
# n = 5
# 想想所有可能, 分左右树来思考
#  见图吧

class Solution(object):
    def __init__(self):
        self.hashmap = {}

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0: return 1
        if n == 2: return 2
        if n == 3: return 5

        # 除去根节点`, 剩下n-1个去构建树
        # 还记得优化的原理,不过 # 第一次把hashmap放在这里(方法中),每次入栈都会清空
        # self.hashmap = {}
        sum = 0
        _tmp = self.hashmap.get(n, None)
        if _tmp != None: return _tmp

        for i in range(0, n):
            # 一共n-1节点,左右分
            sum += self.numTrees(i)*self.numTrees((n-1)-i)
        self.hashmap[n] = sum
        return sum


import time
t1 = time.time()
s = Solution()
rt = s.numTrees(18)
print(time.time() - t1)
print(rt)
print(s.hashmap)
