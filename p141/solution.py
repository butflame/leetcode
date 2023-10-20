# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = fast = head
        while 1:
            if not slow.next or not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True


