# coding:utf-8
# Code date: 20200815


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# leetcode的时间测试和内存测试都不准，变化太大,重在优化思想
#  两个指针比较val， 优化方法是，若重复元素多，右边指针一直右移, 不用一个个拆链表元素
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        p1 = head
        p2 = head.next
        while p2:
            if p2.val != p1.val:
                p2 = p2.next
                p1 = p1.next
            else:  # p2.val == p1.val:
                while p2.next and p2.val == p2.next.val:
                    p2 = p2.next
                p1.next = p2.next  # cut node
                p2 = p2.next  # once step forward
        return head

# establish linked list
head = ListNode(1)
cur = head
for ele in [1, 2, 3, 3, 3]:
    cur.next = ListNode(ele)
    cur = cur.next

s = Solution()
s.deleteDuplicates(head)

cur = head
while cur:
    print(cur.val)
    cur = cur.next


# Input: 1->1->2->3->3
# Output: 1->2->3