from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["anagram", "nagaram"],
                "kwargs": {},
                "expect": True,
            },
            {
                "args": ["car", "rat"],
                "kwargs": {},
                "expect": False
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().isAnagram(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
