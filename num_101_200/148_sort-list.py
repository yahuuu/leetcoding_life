#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/2
# @Author  : yahuuu

from typing import Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.ls = []
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr:
            heapq.heappush(self.ls, ptr.val)
            ptr = ptr.next
        header = None
        ptr = None
        while self.ls:
            min_ele = heapq.heappop(self.ls)
            if header is None:
                header = ListNode(min_ele)
                ptr = header
                continue
            ptr.next = ListNode(min_ele)
            ptr = ptr.next
        return header

if __name__ == '__main__':
    head = [-1, 5, 3, 4, 0]
    header = None
    ptr = None
    for i in head:
        if not header:
            header = ListNode(i, None)
            ptr = header
            continue
        new_node = ListNode(i, None)
        ptr.next = new_node
        ptr = ptr.next

    solu = Solution()
    res = solu.sortList(header)

    ptr = res
    while ptr:
        print(ptr.val)
        ptr = ptr.next
