# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        设环外长度为a, 环内长度为b
        f为快指针走过的长度，s为慢指针走过的长度
        当快慢指针相遇时，一定为：
        - 快指针走过的长度为慢指针的两倍
        - 快指针一定比慢指针多走过n个整环
        于是有：
        - f = 2s
        - f = s + nb
        计算可得：
        - f = 2nb
        - s = nb
        （很tricky但是是真的，相遇时快慢指针走过的步数一定是b的整数倍）
        而某个指针在带环链表内位于环起点时，其从起点开始的步数一定为 a + xb (x为正整数)
        因此在快慢指针相遇后，让其再走a步即可到达环起点
        所以在相遇之后，再用一个指针从起点出发，与慢指针同步前进，则他们一定相遇在环起点

        :param head:
        :return:
        """
        if not head or not head.next:
            return None
        slow = fast = pivot = head
        while 1:
            if not slow.next or not fast.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        while slow != pivot:
            slow = slow.next
            pivot = pivot.next
        return pivot

