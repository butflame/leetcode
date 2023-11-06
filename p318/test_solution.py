from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]],
                "kwargs": {},
                "expect": 16,
            },
            {
                "args": [["a", "ab", "abc", "d", "cd", "bcd", "abcd"]],
                "kwargs": {},
                "expect": 4
            },
            {
                "args": [["a", "aa", "aaa", "aaaa"]],
                "kwargs": {},
                "expect": 0
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().maxProduct(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
