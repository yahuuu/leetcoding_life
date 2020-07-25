# -*- coding:utf-8 -*-
# Created data: 20200723


# https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/

# 简单的链表反转，我快傻了

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        if not head.next: return head
        first = None
        mid = head
        second = head.next
        while second:
            mid.next = first

            first = mid
            mid = second
            second = second.next
        mid.next = first

        return mid


if __name__ == "__main__":
    cur = head = ListNode(0)
    for i in range(1, 10):
        cur.next = ListNode(i)
        cur = cur.next
    cur.next = None

    s = Solution()
    Head = s.reverseList(head)

    while Head:
        print(Head.val)
        Head = Head.next

