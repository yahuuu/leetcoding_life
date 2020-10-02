# -*- coding:utf-8 -*-
# Created data: 20201002

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class BuildTree(object):
    def __init__(self, ls:list, link_num):
        self.head = None
        if ls is None:
            self.head = None
        else:
            node = None
            node_ls = []
            for i in ls:
                if not self.head:
                    self.head = ListNode(i)
                    node = self.head
                    node_ls.append(self.head)
                    continue
                node.next = ListNode(i)
                node = node.next
                node_ls.append(node)
            if link_num != 0:
                node.next = node_ls[link_num]
            print(node_ls)

# 思路：官方要求内存Ｏ（１），自然不能因果哈希表了
# 用两个指针，　１倍速和０．５倍速，指针相交了说明是有环
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        node = head
        node_slow = head  # 速度是二分之一
        i = 0
        while node:
            node = node.next
            if node is node_slow:
                return True
            i += 1
            if i%2 == 0:
                node_slow = node_slow.next
                i = 0
        return False

# 快指针２倍速，和慢指针1倍速
# 指针相交表示有环形存在
class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        node = head
        node_fast= head  # 速度是两倍
        while node_fast:
            node = node.next
            node_fast = node_fast.next
            if node_fast:
                node_fast = node_fast.next
            else:
                return False
            if node is node_fast:
                return True
        return False


if __name__ == "__main__":
    ls = [3, 2, 1, 1, 0]
    tree_root = BuildTree(ls, 2).head
    res = Solution2().hasCycle(tree_root)
    print(res)
