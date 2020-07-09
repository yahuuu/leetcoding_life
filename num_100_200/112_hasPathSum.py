# -*- coding:utf-8 -*-
# Created date: 20200709

# 递归, 第二遍通过,写前考虑好,
# 路径是根节点到叶子,
# 所以叶子条件是什么:没有左右子节点


class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right= None

class binaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, ele):
        if self.root is None:
            self.root = Node(ele)
            return
        node = Node(ele)
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.left is None:
                cur.left = node
                return
            else:
                queue.append(cur.left)

            if cur.right is None:
                cur.right = node
                return
            else:
                queue.append(cur.right)

    def breath_travel(self):
        rt = [self.root]
        while rt:
            cur = rt.pop(0)
            print(cur.val)
            if cur.left is not None: rt.append(cur.left)
            if cur.right is not None: rt.append(cur.right)


class Solution:
    def hasPathSum(self, root, sum):
        if root is None: return False
        self.rt = False
        def search(cur, tmp):
            # 递归的出口是叶子
            if not (cur.left or cur.right):
                # 根到叶子的和判断
                if tmp == sum: self.rt = True
                return
            # 有左节点时候,搜索
            if cur.left:
                search(cur.left, tmp+cur.left.val)
            # 有右节点时候,搜索
            if cur.right:
                search(cur.right, tmp+cur.right.val)
        search(root, root.val)

        return self.rt


if __name__ == "__main__":
    ls = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    tree = binaryTree()
    for ele in ls:
        tree.add(ele)
    # tree.breath_travel()
    s = Solution()
    s.hasPathSum(tree.root, 22)
