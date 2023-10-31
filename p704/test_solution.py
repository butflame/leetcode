from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            # {
            #     "args": [[-1, 0, 3, 5, 9, 12], 9],
            #     "kwargs": {},
            #     "expect": 4
            # },
            # {
            #     "args": [[-1, 0, 3, 5, 9, 12], 2],
            #     "kwargs": {},
            #     "expect": -1
            # },
            {
                "args": [[0], 0],
                "kwargs": {},
                "expect": 0
            },
            {
                "args": [[0, 1], 1],
                "kwargs": {},
                "expect": 1
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().search(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
