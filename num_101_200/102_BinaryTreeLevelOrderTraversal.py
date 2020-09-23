# coding:utf-8
# Code date: 20200


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if not root: return []
        rt = []
        stack = [root]
        while stack:
            n = len(stack)  # n恰好是本层的node数量
            level_rt = []
            for i in range(n):
                cur = stack.pop(0)
                if cur.val is not None:
                    level_rt.append(cur.val)
                if cur.left is not None:
                    stack.append(cur.left)
                if cur.right is not None:
                    stack.append(cur.right)
            rt.append(level_rt)
        return rt