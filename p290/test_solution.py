from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["abba", "dog cat cat dog"],
                "kwargs": {},
                "expect": True,
            },
            {
                "args": ["abba", "dog cat cat fish"],
                "kwargs": {},
                "expect": False
            },
            {
                "args": ["aaaa", "dog cat cat dog"],
                "kwargs": {},
                "expect": False
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().wordPattern(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
