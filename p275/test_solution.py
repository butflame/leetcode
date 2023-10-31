from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[0, 1, 4, 5, 6, 9]],
                "kwargs": {},
                "expect": 4
            },
            {
                "args": [[0, 1, 4, 5, 6]],
                "kwargs": {},
                "expect": 3
            },
            {
                "args": [[1, 2, 100]],
                "kwargs": {},
                "expect": 2
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().hIndex(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
