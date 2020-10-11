# -*- coding:utf-8 -*-
# Created data: 20201011


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 在我第一次写之前我没有想好思路，着急敲了
# 没想好就是瞎写
# 思路： 递归,不断分割前序和中序的数组
# 前序: 根+左遍历+右遍历
# 中序: 左遍历+根+右遍历
# 前序的第一个节点在中序的索引，将中序分为左,根, 右树， 可以得到左右树的个数
# 依据左右树的个数来分割前序数组为根，左，右
# 前序数组的左,右分别递归
# time: O(N) + mem: O(N)
# 内存的使用情况： hashmap O(N), return构造好的树 O(N), 递归时候的栈的深度即树的高度 O(h)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return
            # 前序的第一个节点就是根节点, 根+左+右
            tree_root = TreeNode(preorder[pre_left]) # 构造根节点

            root_in_inorder_idx = in_idx[preorder[pre_left]] # 根节点在中序数组中的索引
            lef_subtree_num = root_in_inorder_idx - in_left
            # right_subtree_num = in_right - root_in_inorder_idx
            tree_root.left = helper(pre_left+1, pre_left+lef_subtree_num, in_left, root_in_inorder_idx - 1) # 构造左节点
            tree_root.right = helper(pre_left+lef_subtree_num+1, pre_right, root_in_inorder_idx + 1, in_right) # 右节点
            return tree_root

        in_idx = {ele: idx for idx, ele in enumerate(inorder)}
        return helper(pre_left=0, pre_right=len(preorder)-1,\
                      in_left=0, in_right=len(preorder)-1)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solu = Solution()
    tree_root = solu.buildTree(preorder, inorder)
    print()