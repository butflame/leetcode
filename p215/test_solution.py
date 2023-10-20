from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[3, 2, 1, 5, 6, 4], 2],
                "kwargs": {},
                "expect": 5
            },
            {
                "args": [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
                "kwargs": {},
                "expect": 4
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().findKthLargest(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
