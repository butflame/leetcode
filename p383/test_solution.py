from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["a", "b"],
                "kwargs": {},
                "expect": False,
            },
            {
                "args": ["aa", "ab"],
                "kwargs": {},
                "expect": False
            },
            {
                "args": ["aa", "aab"],
                "kwargs": {},
                "expect": True
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().canConstruct(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
