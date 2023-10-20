from unittest import TestCase

from .solution import Solution, ListNode


class Test(TestCase):
    def test_1(self):
        values = [3, 2, 0, -4]
        pos = 1
        inp = build_linked_list(values, pos)
        expect = nth_node(inp, pos) if pos >= 0 else None
        case = {
            "args": [inp],
            "kwargs": {},
            "expect": expect
        }
        result = Solution().detectCycle(*case["args"], **case["kwargs"])
        expect = case["expect"]
        self.assertIs(result, expect)

    def test_2(self):
        values = [1, 2]
        pos = 0
        inp = build_linked_list(values, pos)
        expect = nth_node(inp, pos) if pos >= 0 else None
        case = {
            "args": [inp],
            "kwargs": {},
            "expect": expect
        }
        result = Solution().detectCycle(*case["args"], **case["kwargs"])
        expect = case["expect"]
        self.assertIs(result, expect)

    def test_3(self):
        values = [1]
        pos = -1
        inp = build_linked_list(values, pos)
        expect = nth_node(inp, pos) if pos >= 0 else None
        case = {
            "args": [inp],
            "kwargs": {},
            "expect": expect
        }
        result = Solution().detectCycle(*case["args"], **case["kwargs"])
        expect = case["expect"]
        self.assertIs(result, expect)

    def test_4(self):
        values = [1, 2]
        pos = -1
        inp = build_linked_list(values, pos)
        expect = nth_node(inp, pos) if pos >= 0 else None
        case = {
            "args": [inp],
            "kwargs": {},
            "expect": expect
        }
        result = Solution().detectCycle(*case["args"], **case["kwargs"])
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
