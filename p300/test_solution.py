from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            # {
            #     "args": [[10, 9, 2, 5, 3, 7, 101, 18]],
            #     "kwargs": {},
            #     "expect": 4
            # },
            # {
            #     "args": [[0, 1, 0, 3, 2, 3]],
            #     "kwargs": {},
            #     "expect": 4
            # },
            # {
            #     "args": [[7, 7, 7, 7, 7, 7, 7]],
            #     "kwargs": {},
            #     "expect": 1
            # },
            {
                "args": [[1, 3, 6, 7, 9, 4, 10, 5, 6]],
                "kwargs": {},
                "expect": 6
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().lengthOfLIS(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
