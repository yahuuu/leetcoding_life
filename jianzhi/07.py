# -*- coding:utf-8 -*-
# Created data: 20200724


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 这道题要求使用前序和中序遍历来恢复二叉树,树中没有重复元素
# 思路： 首先能根据前序和中序推导手绘广度优先遍历的二叉树
# 其次在递归处理中序子串时， 务必要计算好下标，
# 难点在每层递归中，计算好根节点在前序中的下标idx: pre_idx+(mid_root_idx-in_l_idx+1)
# 难点解析： 关于上面的公式，pre_idx没的说，就是先序的索引, 加上
# 递归要记得出栈口
#       3
#    /    \
#   9      20
#  / \   /   \
# 1   2  15   7
# 前序遍历 preorder = [3, 9,1,2 ,20,15,7] # 根+左子树+右子树
# 中序遍历  inorder = [1,9,2, 3, 15,20,7] # 左子树+根+右子树
class Solution:
    def buildTree(self, preorder, inorder): # List[int], inorder: List[int]) -> TreeNode:
        def recur(pre_idx, in_l_idx, in_r_idx):
            if in_l_idx > in_r_idx:
                return
            root = TreeNode(preorder[pre_idx])
            mid_root_idx = dict[preorder[pre_idx]]  # 先序节点在中序的idx
            root.left = recur(pre_idx+1, in_l_idx, mid_root_idx-1)
            root.right = recur(pre_idx+(mid_root_idx-in_l_idx+1), mid_root_idx+1, in_r_idx)
            #                  pre_idx+(mid_root_idx-in_l_idx+1)
            #      根节点在pre中下标    +    左子树的长度  +      向右移动一位
            #       0                 +     3-           0   +1
            return root

        if preorder == []: return None
        # 缓存中序的索引
        dict = {ele:idx for idx, ele in enumerate(inorder)}
        # for i in range(preorder):
        return recur(0, 0, len(inorder)-1)
