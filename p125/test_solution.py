from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["A man, a plan, a canal: Panama"],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ["race a car"],
                "kwargs": {},
                "expect": False
            },
            {
                "args": [" "],
                "kwargs": {},
                "expect": True
            },

        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().isPalindrome(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
