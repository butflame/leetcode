from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [["flower", "flow", "flight"]],
                "kwargs": {},
                "expect": "fl"
            },
            {
                "args": [["dog", "racecar", "car"]],
                "kwargs": {},
                "expect": ""
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().longestCommonPrefix(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
