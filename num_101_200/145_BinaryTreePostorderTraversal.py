# coding:utf-8
# Code date: 20200915

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_recur:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        def helper(node):
            if not node: return
            helper(node.left)
            helper(node.right)
            res.append(node.val)
        helper(root)
        return res

# 栈方法来实现，写了很长时间
# ONCE AC， 太值了
# 先把左树的节点加入， 然后弹栈元素
# 弹出的元素要注意是否有右节点, 没有好办，直接res记录
# 有的话需要在右子树收集所有左树节点， 切记断开此时的右子树
# 我修改了树的结构，为了循环逻辑实现方便
#              1
#            /     断开
#         2           3
class Solution_stack:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = [root]
        res = []
        while stack[-1].left:
            stack.append(stack[-1].left)
        while stack:
            node = stack.pop()
            if not node.right:
                res.append(node.val)
            else:
                # res.append(node.right.val)
                stack.append(node)
                stack.append(node.right)
                while stack[-1].left:   # 再次遍历子左树
                    stack.append(stack[-1].left)
                node.right = None  # 拆树右枝
        return res

#              1
#         2          3
#      4     5    7      8
#  11 12   13  14
#        21 22
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

if __name__ == "__main__":
    root = tree()
    solu = Solution_recur()
    res = solu.postorderTraversal(root)
    print(res)
    root = tree()
    solu = Solution_stack()
    res = solu.postorderTraversal(root)
    print(res)
