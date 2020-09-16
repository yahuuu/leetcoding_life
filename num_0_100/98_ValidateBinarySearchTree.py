# coding:utf-8
# Code date: 20200914



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 我并没有度完全理解二叉搜索树的定义，实际上原题写的也很懒
# 我的解法只能验证每个节点都是左小于根节点，右大于根节点
# 我写的是一棵从上往下的递归树
class NoSolution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node):
            if not node:
                return True
            if not node.left and not node.right:
                return True

            res = True
            if node.left:
                if node.left.val >= node.val:
                    res = False

            if node.right:
                if node.right.val <= node.val:
                    res = False
            return res and helper(node.left) and helper(node.right)

        if not root:
            return True
        return helper(root)

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 仔细思考这两句话，你可以理解为：
# 当前节点的值是其左子树的值的上界（最大值）
# 当前节点的值是其右子树的值的下界（最小值）
# 上面的话很好，很透彻，对理解题意很有帮助，
# 出自： https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yi-zhang-tu-rang-ni-ming-bai-shang-xia-jie-zui-da-/
# time O(N), mem O(N)
class Solution_official:
    """这也是一棵从上往下的递归树"""
    def isValidBST(self, root):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

# Todo: 我还没有掌握
class Solution_official1:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    # root.left.left = TreeNode(-1)
    # root.left.right = TreeNode(2)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)

    solu = Solution_official1()
    res = solu.isValidBST(root)
    print(res)

    # 5
   # / \
  # 1   6
  #    / \
  #   3   7
