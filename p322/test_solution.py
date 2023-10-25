from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            # {
            #     "args": [[1, 2, 5], 11],
            #     "kwargs": {},
            #     "expect": 3
            # },
            {
                "args": [[2], 3],
                "kwargs": {},
                "expect": -1
            },
            {
                "args": [[1], 0],
                "kwargs": {},
                "expect": 0
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().coinChange(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
