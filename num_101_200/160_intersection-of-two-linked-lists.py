# -*- coding: utf-8 -*-
# @Time    : 2021/7/2 上午7:52
# @Author  : yahuuu
# @FileName: 160_intersection-of-two-linked-lists.py
# @Software: PyCharm


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        ptrA = headA; ptrB = headB
        while ptrA or ptrB:
            ptrA.a = 1
            ptrB.b = 1
            if hasattr(ptrA, "b"):
                return ptrA
            if hasattr(ptrB, "a"):
                return ptrB
            if ptrA.next:
                ptrA = ptrA.next
            if ptrB.next:
                ptrB = ptrB.next
            if not ptrA.next and not ptrB.next:
                if ptrA is ptrB: return ptrA
                break
        return None