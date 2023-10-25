from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [2],
                "kwargs": {},
                "expect": 2
            },
            {
                "args": [3],
                "kwargs": {},
                "expect": 3
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().climbStairs(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
