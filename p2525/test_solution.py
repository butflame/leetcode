from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [1000, 35, 700, 300],
                "kwargs": {},
                "expect": "Heavy"
            },
            {
                "args": [200, 50, 800, 50],
                "kwargs": {},
                "expect": "Neither"
            },
            {
                "args": [3223, 1271, 2418, 749],
                "kwargs": {},
                "expect": "Both"
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().categorizeBox(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
