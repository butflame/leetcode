from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[1, 2, 3]],
                "kwargs": {},
                "expect": [1, 2, 4]
            },
            {
                "args": [[4, 3, 2, 1]],
                "kwargs": {},
                "expect": [4, 3, 2, 2]
            },
            {
                "args": [[0]],
                "kwargs": {},
                "expect": [1]
            },
            {
                "args": [[1, 0]],
                "kwargs": {},
                "expect": [1, 1]
            },
            {
                "args": [[1, 9]],
                "kwargs": {},
                "expect": [2, 0]
            },
            {
                "args": [[9, 9]],
                "kwargs": {},
                "expect": [1, 0, 0]
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().plusOne(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
