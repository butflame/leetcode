from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[1, 8, 6, 2, 5, 4, 8, 3, 7]],
                "kwargs": {},
                "expect": 49
            },
            {
                "args": [[1, 1]],
                "kwargs": {},
                "expect": 1
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().maxArea(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
