from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [7],
                "kwargs": {},
                "expect": 1
            },
            {
                "args": [121],
                "kwargs": {},
                "expect": 2
            },
            {
                "args": [1248],
                "kwargs": {},
                "expect": 4
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().countDigits(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
