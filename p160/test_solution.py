from unittest import TestCase

from .solution import Solution, ListNode


class Test(TestCase):
    def test_1(self):
        tail = build_linked_list([8, 4, 5], -1)
        head1 = build_linked_list([4, 1], -1)
        head2 = build_linked_list([5, 6, 1], -1)
        nth_node(head1, 1).next = tail
        nth_node(head2, 2).next = tail

        expect = nth_node(tail, 0)
        case = {
            "args": [head1, head2],
            "kwargs": {},
            "expect": expect
        }
        result = Solution().getIntersectionNode(*case["args"], **case["kwargs"])
        expect = case["expect"]
        self.assertIs(result, expect)


def build_linked_list(values, pos):
    ret = []
    if not values:
        return
    for i in values:
        ret.append(ListNode(i))
    for i in range(len(ret) - 1):
        ret[i].next = ret[i + 1]
    if pos >= 0:
        ret[-1].next = ret[pos]
    return ret[0]


def nth_node(head, n):
    while n > 0:
        head = head.next
        n -= 1
    return head
