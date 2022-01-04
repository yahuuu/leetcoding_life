# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
优先队列，最小堆应该早点学学，
注意内存的消耗，这道题可以每次只把k个元素放到最小堆里
"""

import heapq
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.ls = list()
        self.dummy_node = self.ptr = ListNode(-1)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def __lt__(self, other: ListNode):
            return self.val < other.val
        ListNode.__lt__ = __lt__
        for node in lists:
            if node:
                heapq.heappush(self.ls, node)
        while self.ls:
            node = heapq.heappop(self.ls)
            self.ptr.next = ListNode(node.val)
            self.ptr = self.ptr.next
            if node.next is not None:
                heapq.heappush(self.ls, node.next)
        return self.dummy_node.next


if __name__ == '__main__':
    a = ListNode(0)
    a.next = ListNode(1)
    b = ListNode(1)
    b.next = ListNode(2)
    b.next.next = ListNode(3)
    c = ListNode(0)
    c.next = ListNode(4)
    ls = [a, b, c]
    solu = Solution()
    ptr = solu.mergeKLists(ls)
    while ptr:
        print(ptr.val)
        ptr = ptr.next
