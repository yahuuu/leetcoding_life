# -*- coding:utf-8 -*-
# Created data: 20200724


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思路： 首先能根据前序和中序推导手绘广度优先遍历的二叉树
# 其次在递归处理中序子串时， 务必要计算好下标，
# 难点在每层递归中，计算好根节点在前序中的下标idx: pre_idx+(mid_root_idx-in_l_idx+1)
# 递归要记得出栈口
class Solution:
    def buildTree(self, preorder, inorder): # List[int], inorder: List[int]) -> TreeNode:
        def recur(pre_idx, in_l_idx, in_r_idx):
            if in_l_idx > in_r_idx:
                return
            root = TreeNode(preorder[pre_idx])
            mid_root_idx = dict[preorder[pre_idx]]
            root.left = recur(pre_idx+1, in_l_idx, mid_root_idx-1)
            root.right = recur(pre_idx+(mid_root_idx-in_l_idx+1), mid_root_idx+1, in_r_idx)
            return root

        if preorder == []: return None
        dict = {ele:idx for idx, ele in enumerate(inorder)}
        # for i in range(preorder):
        return recur(0, 0, len(inorder)-1)

