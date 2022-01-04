
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        ls = list()
        current = head
        new_head = head
        stack_first_ptr = None
        while current:
            for i in range(k):
                ls.append(current)
                current = current.next
                if not current:
                    break
            if len(ls) < k:
                # 链接下一个节点要分情况
                next_group = ls[0]
                if stack_first_ptr:
                    # 长度不足k，直接链接原来的字串返回
                    stack_first_ptr.next = next_group
                return new_head
            else:
                next_group = ls[-1]
            if head == new_head:
                new_head = ls[-1]
            if stack_first_ptr:
                stack_first_ptr.next = next_group # 连接到下一栈最底层元素
            ptr = stack_first_ptr = ls.pop()
            while ls:
                ptr.next = ls.pop()
                ptr = ptr.next
            stack_first_ptr = ptr
        stack_first_ptr.next = None
        return new_head


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    solu =  Solution()
    head = solu.reverseKGroup(a, k=3)
    while head:
        print(head.val)
        head = head.next