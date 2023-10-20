from unittest import TestCase

from .solution import Solution, ListNode


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [build_linked_list([3, 2, 0, -4], 1)],
                "kwargs": {},
                "expect": True
            },
            {
                "args": [build_linked_list([1, 2], 0)],
                "kwargs": {},
                "expect": True
            },
            {
                "args": [build_linked_list([1], -1)],
                "kwargs": {},
                "expect": False
            },
            {
                "args": [build_linked_list([1, 2], -1)],
                "kwargs": {},
                "expect": False
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().hasCycle(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")


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
