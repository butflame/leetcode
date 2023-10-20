from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["III"],
                "kwargs": {},
                "expect": 3
            },
            {
                "args": ["IV"],
                "kwargs": {},
                "expect": 4
            },
            {
                "args": ["IX"],
                "kwargs": {},
                "expect": 9
            },
            {
                "args": ["LVIII"],
                "kwargs": {},
                "expect": 58
            },
            {
                "args": ["MCMXCIV"],
                "kwargs": {},
                "expect": 1994
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().romanToInt(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
