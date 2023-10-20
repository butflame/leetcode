from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[2, 3, 4, 6]],
                "kwargs": {},
                "expect": 8
            },
            {
                "args": [[1, 2, 4, 5, 10]],
                "kwargs": {},
                "expect": 16
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().tupleSameProduct(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
