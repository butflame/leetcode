from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["Hello World"],
                "kwargs": {},
                "expect": 5
            },
            {
                "args": ["   fly me   to   the moon  "],
                "kwargs": {},
                "expect": 4
            },
            {
                "args": ["luffy is still joyboy"],
                "kwargs": {},
                "expect": 6
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().lengthOfLastWord(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
