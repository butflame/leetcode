from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[1, 3, 5, 6], 5],
                "kwargs": {},
                "expect": 2
            },
            {
                "args": [[1, 3, 5, 6], 2],
                "kwargs": {},
                "expect": 1
            },
            {
                "args": [[1, 3, 5, 6], 7],
                "kwargs": {},
                "expect": 4
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().searchInsert(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
