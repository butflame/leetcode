from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["abc", "ahbgdc"],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ["axc", "ahbgdc"],
                "kwargs": {},
                "expect": False
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().isSubsequence(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
