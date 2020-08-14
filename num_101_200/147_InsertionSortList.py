# -*- coding:utf-8 -*-
# Created data: 20200712


# 不是本题答案,只是练习插入排序
class solution1(object):
    def insertionSortList(self, ls):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        for i in range(1, len(ls)):
            for j in range(i, 0, -1):
                if ls[j] < ls[j-1]:
                    ls[j], ls[j-1] = ls[j-1], ls[j]
                else:
                    break
        print(ls)

import random
ls = [random.randint(1,100) for _ in range(10)]
print(ls)
s = solution1()
s.insertionSortList(ls)


# answer
# 思路:我这里直接用最优思路来写的
# 从前到后比较Node的值,
# 不满足从小到大就从链表中摘除
# 摘除点从前到后插入原来链表
# 改进点，建立哨兵节点dummy_head，便于从头开始查找合适的插入位置,无需处理head更新的情况；
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        # 增加一个新节点主要为了比较方便,
        # 顺便了处理了单节点的情况
        new_head = ListNode(float("-inf"))
        new_head.next = head
        p1 = new_head
        p2 = new_head.next
        while p2 != None:
            if p1.val < p2.val:
                p1 = p2
                p2 = p2.next
            else:
                # 不满足从小到大
                tmp_node = p2
                p2 = p2.next # 摘除p2
                p1.next = p2
                point = new_head
                # 寻找插入的点
                while tmp_node.val > point.next.val:
                    point = point.next
                # 插入
                tmp_node.next = point.next
                point.next = tmp_node
        return new_head.next

