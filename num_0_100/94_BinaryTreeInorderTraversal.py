# coding:utf-8
# Code date: 20200915


# Definition for a binary tree node.
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 思路：栈结构，先收集左树，每个节点检查有没有右节点
# 如果有右节点需要在该节点上收集左树
# 写这个前序遍历相当费脑子
# tim,mem: O(n), O(n)
# ONCE AC, 但是时间不占优势,提交了几次，time exceed 变化真大
# 这里没有递归，不合理啊
# 和递归不同的是，栈需要显式来维护数据结构
class Solution1_stack:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        stack = [root]
        # 先收集左树
        while stack[-1].left: # is not None:
            stack.append(stack[-1].left)
        while stack:
            node = stack.pop(-1)
            res.append(node.val)
            if node.right:
                stack.append(node.right)
                while stack[-1].left:
                    stack.append(stack[-1].left)
        return res


# 和栈不同的是，递归隐形栈结构
class Solution2_recur:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        return res


def tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(8)
    root.left.left.left = TreeNode(11)
    root.left.left.right = TreeNode(12)
    root.left.right.left = TreeNode(13)
    root.left.right.right = TreeNode(14)
    root.left.right.left.left = TreeNode(21)
    root.left.right.left.right = TreeNode(22)
    return root
#              1
#         2        3
#      4     5     7    8
#  11 12   13  14
#        21 22
# 4,2,5,1,7,3,8
if __name__ == "__main__":
    root = tree()
    solu = Solution1()
    res = solu.inorderTraversal(root)
    print(res)
    solu = Solution2()
    res = solu.inorderTraversal(root)
    print(res)
