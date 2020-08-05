# coding:utf-8
# Code date: 20200805


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l1 or l2  # 返回为真的对象
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l2, l1.next)
            return l1

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        p1 = l1; p2 = l2
        # 1 2 3 4
        #  6, 7, 8
        root = None
        while p1 or p2:
            if not p1: # p1到尾
                cur.next = p2
                break
            if not p2:
                cur.next = p1
                break
            if p1.val < p2.val:
                if not root:
                    root = p1
                    cur = root
                else:
                    cur.next = p1
                    cur = cur.next
                p1 = p1.next
            else:
                if not root:
                    root = p2
                    cur = root
                else:
                    cur.next = p2
                    cur = cur.next
                p2 = p2.next
            # cur = cur.next

        return root

l2 = ListNode(6)
l2.next = ListNode(7)
l2.next.next = ListNode(8)

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(9)

# cur = root = None
# for i in range(1,3):
#     if not root:
#         root = ListNode(0)
#         cur = root
#     cur.next = ListNode(i)
#     cur= cur.next

s = Solution()
res = s.mergeTwoLists(l2 = l2 , l1 = l1)
while res:
    print(res.val)
    res = res.next
