# -*- coding:utf-8 -*-
# Created data: 2020906

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 广度优先遍历的核心是用队列,node先先进先出
class buildTree(object):
    def __init__(self):
        self.root = None
    # 这是我写过最繁琐的二叉树的构建
    # 时间复杂度不好,以后不打算这么写了
    def add_node(self, ele):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = TreeNode(ele)
                return
            elif node.right is None:
                node.right = TreeNode(ele)
                return
            queue.append(node.left)
            queue.append(node.right)

    def establish(self, ls):
        for ele in ls:
            if self.root is None:
                self.root = TreeNode(ele)
            self.add_node(ele)
        return self.root

    def establish_abd(self, ls: list):
        if not ls: return None
        queue = []
        for ele in ls:
            if not self.root:
                self.root = TreeNode(ele)
                queue.append(self.root)
                continue
            while queue:
                node = queue.pop(0)
                if node.left is None:
                    node.left = TreeNode(ele)
                    queue.insert(0, node)
                    break
                elif node.right is None:
                    node.right = TreeNode(ele)
                    queue.append(node.left)
                    queue.append(node.right)
                    break
                else:
                    pass
        return self.root


def breath_travel(root):
    if root is None:
        print(None); return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == "__main__":
    ls1 = [i for i in range(1, 16)]
    ls2 = [i for i in range(1, 15)]
    tree_root1 = buildTree().establish(ls1)
    tree_root2 = buildTree().establish(ls2)
    # breath_travel(tree_root1)
    # breath_travel(tree_root2)
    solu = Solution().isSameTree(tree_root1, tree_root2)
    print(solu)












