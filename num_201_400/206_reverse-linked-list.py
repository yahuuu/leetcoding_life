# -*- coding: utf-8 -*-
# @Time    : 2021/11/21 下午5:05
# @Author  : yahuuu
# @FileName: 206_reverse-linked-list.py
# @Software: PyCharm


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        p = None
        h = head
        n = head.next
        while n is not None:
            h.next = p
            p = h
            h = n
            n = n.next
        h.next = p
        return h
