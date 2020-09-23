# coding:utf-8
# Code date: 20200914

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop(-1)
            res.append(node.val)
            # pop left node first, push in stack first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(0)

    solu = Solution()
    res = solu.preorderTraversal(root)
    print(res)
