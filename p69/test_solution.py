from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [4],
                "kwargs": {},
                "expect": 2
            },
            {
                "args": [8],
                "kwargs": {},
                "expect": 2
            },
            {
                "args": [24],
                "kwargs": {},
                "expect": 4
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().mySqrt(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
