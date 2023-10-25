from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            # {
            #     "args": [[1, 2, 3, 1]],
            #     "kwargs": {},
            #     "expect": 4
            # },
            # {
            #     "args": [[2, 7, 9, 3, 1]],
            #     "kwargs": {},
            #     "expect": 12
            # },
            {
                "args": [[2, 1, 1, 2]],
                "kwargs": {},
                "expect": 4
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().rob(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
