from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["()"],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ["()[]{}"],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ["(]"],
                "kwargs": {},
                "expect": False
            },
            {
                "args": ["([)]"],
                "kwargs": {},
                "expect": False
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().isValid(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
