# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"<{self.__class__.__name__}> {self.val}"


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        a, b = headA, headB
        switchedA, switchedB = False, False
        while 1:
            if a is b:
                return a
            if a.next:
                a = a.next
            elif not switchedA:
                a = headB
                switchedA = True
            else:
                return None

            if b.next:
                b = b.next
            elif not switchedB:
                b = headA
                switchedB = True
            else:
                return None
