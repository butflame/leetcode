from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[7, 1, 5, 3, 6, 4]],
                "kwargs": {},
                "expect": 7
            },
            {
                "args": [[1, 2, 3, 4, 5]],
                "kwargs": {},
                "expect": 4
            },
            {
                "args": [[7, 6, 4, 3, 1]],
                "kwargs": {},
                "expect": 0
            },

        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().maxProfit(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
