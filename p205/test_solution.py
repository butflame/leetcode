from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["egg", "add"],
                "kwargs": {},
                "expect": True,
            },
            {
                "args": ["bar", "foo"],
                "kwargs": {},
                "expect": False
            },
            {
                "args": ["foo", "bar"],
                "kwargs": {},
                "expect": False
            },
            {
                "args": ["aa", "cc"],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ["paper", "title"],
                "kwargs": {},
                "expect": True
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().isIsomorphic(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
