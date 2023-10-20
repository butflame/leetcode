from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["sadbutsad", "sad"],
                "kwargs": {},
                "expect": 0
            },
            {
                "args": ["leetcode", "leeto"],
                "kwargs": {},
                "expect": -1
            },

        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().strStr(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
