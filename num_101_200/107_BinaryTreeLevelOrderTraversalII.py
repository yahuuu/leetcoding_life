# -*- coding:utf-8 -*-
# Created data: 2020912


from typing import List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(ls):
    root = TreeNode(ls[0])
    root.left = TreeNode(ls[1])
    root.right = TreeNode(ls[2])
    root.left.left = TreeNode(ls[3])
    # root.right.left = TreeNode(ls[5])
    root.right.right = TreeNode(ls[6])
    return root

# 广度优先遍历
# 这里我在显式的控制层次,用字典记录
# 也可以不用字典,用两个list,一个一直记录层次,入栈的数值和栈顶数值不同时,表示新层
# 看了官方的题解,比我要省下一个O(N)的内存开销,思路二就不写了
# 而官方思路: 是取queue的长度,因为len(queue)刚好是本层所有的节点
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(list)
        queue = [(root, 0)]
        while queue:
            node, layer = queue.pop(0)
            res[layer].append(node.val)
            if node.left:
                queue.append((node.left, layer+1))
            if node.right:
                queue.append((node.right, layer+1))
        return list(res.values())[::-1]


if __name__ == "__main__":
    ls = [1,2,3,4,"null","null",5]
    root = build_tree(ls)
    solu = Solution()
    res = solu.levelOrderBottom(root)
    print(res)

    # from line_profiler import LineProfiler
    # lp = LineProfiler()
    # lp.add_function(Solution.groupAnagrams)  # 被引用函数需要声明才显示细节
    # lp_wrapper = lp(Solution().levelOrderBottom)  # 被显示的函数
    # lp_wrapper(root)  # 参数传入
    # lp.print_stats()  # 打印喽