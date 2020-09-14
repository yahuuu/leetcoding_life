# coding:utf-8
# Code date: 20200909

# Definition for a binary tree node.
# TODO：从上到下，从下到上的递归树，区别我还不是很熟悉
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 平衡二叉树的条件是每个节点的左右子树高度差不超过1
# 高度指的是从根节点到最深层的叶子节点的总长度
# 自顶向下的递归
class Solution_official:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node: TreeNode) -> int:
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1

        if not root:
            return True

        # 每个节点都会从遍历一遍完整的子树
        # 树的高度是O(logN)
        return abs(height(root.left) - height(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)

# 核心：到底是自顶向下还是自下向上要注意看return 的返回值
# 若还不明白，就在脑海中划一棵递归生成的树
# 这道题的最优思路是自顶向下的递归
class Solution_official2:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            # 这里的节点的确只会计算一遍高度
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0



if __name__ == "__main__":
    # ls = [3, 9, 20, "null", "null", 15, 7]
    ls = [1, 2,2 , 3,3 ,None,None,4,4]
    #          1
    #     2           2
    #  3     3      n   n
    # 4 4
    root = TreeNode(ls[0])
    root.left  = TreeNode(ls[1])
    root.right = TreeNode(ls[2])
    root.left.left  = TreeNode(ls[3])
    root.left.right = TreeNode(ls[4])
    root.right.left  = None # TreeNode(ls[5])
    root.right.right = None # TreeNode(ls[6])
    root.left.left.left  = TreeNode(ls[7])
    root.left.left.left  = TreeNode(ls[8])
    # solu = Solution_official().isBalanced(root)
    solu = Solution_official2().isBalanced(root)
    print(solu)
