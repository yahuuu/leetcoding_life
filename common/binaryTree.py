# -*- coding:utf-8 -*-

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


if __name__ == "__main__":
    ls = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    tree = binaryTree()
    for ele in ls:
        tree.add(ele)
    tree.breath_travel()
