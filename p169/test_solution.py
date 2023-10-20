from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[3, 2, 3]],
                "kwargs": {},
                "expect": 3
            },
            {
                "args": [[2, 2, 1, 1, 1, 2, 2]],
                "kwargs": {},
                "expect": 2
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().majorityElement(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
