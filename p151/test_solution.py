from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["the sky is blue"],
                "kwargs": {},
                "expect": "blue is sky the"
            },
            {
                "args": ["  hello world  "],
                "kwargs": {},
                "expect": "world hello"
            },
            {
                "args": ["a good   example"],
                "kwargs": {},
                "expect": "example good a"
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().reverseWords(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
