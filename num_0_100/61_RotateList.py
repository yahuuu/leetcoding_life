# -*- coding:utf-8 -*-
# Created data: 2020828


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# https://leetcode-cn.com/problems/rotate-list/
# 移动后面k个节点到链表头部
# 思路: 在移动链表之前先判断有效需要移动多少元素,
# 否则链表有5个元素, 移动十次相当于没有移动对吧
# time win: 97% ,mem win: 43%

# 1, 2, 3, 4, 5
# k = 2
# 4, 5, 1, 2, 3
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # just count num of linked list
        if not head: return None
        if not k: return head
        cur = head
        num = 0
        while cur:
            num += 1
            cur = cur.next
        if num == 1: return head  # 一节点直接扔回去,不用移动
        if k==num: return head
        if k>num: k = k%num
        if not k: return head  # 保证移动倍数节点,直接返回head

        cur = head
        cut_node = None
        # 向后移动k个节点
        for i in range(k):
            cur = cur.next
        cut_node = head
        while cur.next:
            cur = cur.next
            cut_node = cut_node.next
        # print(cut_node.val)
        tmp = cut_node.next
        cut_node.next = None
        cur.next = head
        return tmp

        # k = 3
        # 1, 2, 3, 4, 5
        #    |        |
        # cut_node就是要移动到链表前面的点
        # cur.next = head


if __name__ == "__main__":
    input_ls = [1, 2, 3, 4, 5]
    k = 10
    # input_ls = [1]
    # k = 99
    # build linked list
    cur = head = None
    for ele in input_ls:
        if not head:
            head = ListNode(ele)
            cur = head
            continue
        cur.next = ListNode(ele)
        cur = cur.next

    cur = head
    while cur:
        # print(cur.val)
        cur = cur.next

    solu = Solution()
    head = solu.rotateRight(head, k=k)

    # just print
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
