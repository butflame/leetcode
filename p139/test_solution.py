from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["ab", ["a", "b"]],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ["leetcode", ["leet", "code"]],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ["applepenapple", ["apple", "pen"]],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
                "kwargs": {},
                "expect": False
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().wordBreak(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
