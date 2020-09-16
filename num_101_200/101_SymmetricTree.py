# coding:utf-8
# Code date: 20200916

    # 1
   # / \
  # 2   2
 # / \ / \
# 3  4 4  3

def build_tree(ls):
    root = TreeNode(ls[0])
    root.left = TreeNode(ls[1])
    root.right = TreeNode(ls[2])
    root.left.left = TreeNode(ls[3])
    root.left.right = TreeNode(ls[4])
    root.right.left = TreeNode(ls[5])
    root.right.right = TreeNode(ls[6])
    return root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 时间复杂度是O(2N)
# 提交time  && mem  都变化很大
class Solution_queue:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        queue = [root]
        while queue:
            queue = [i for ele in queue for i in [ele.left, ele.right]]
            pointl= 0; pointr = len(queue)-1
            if not any(queue):
                break
            while pointl < pointr:  # 偶数不可以相等
                if not queue[pointl] and not queue[pointr]:
                    pointl += 1
                    pointr -= 1
                    continue
                if queue[pointl] is None and queue[pointr]:
                    return False
                if queue[pointr] is None and queue[pointl]:
                    return False
                if queue[pointl].val != queue[pointr].val:
                    return False
                pointl += 1
                pointr -= 1
            queue = [i for i in queue if i]  # 对比完后清除None元素 #额外O(N)
        return True

# 来自网上的一段递归思路，评论中的的一段思路
# https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode-solution/
# 我在实现时候没有考虑好对称性，
class Solution_recur:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2:
                return False
            if not node2 and node1:
                return False
            return node1.val == node2.val\
                   and helper(node1.left, node2.right)\
                   and helper(node1.right, node2.left)

        if not root:
            return True
        res = helper(root.left, root.right)
        return res


if __name__ == "__main__":
    ls = [1, 2, 2, 3, 4, 4, 3]
    root = build_tree(ls)
    solu = Solution_recur()
    res = solu.isSymmetric(root)
    print(res)