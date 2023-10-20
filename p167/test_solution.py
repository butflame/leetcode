from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[2, 7, 11, 15], 9],
                "kwargs": {},
                "expect": [1, 2]
            },
            {
                "args": [[2, 3, 4], 6],
                "kwargs": {},
                "expect": [1, 3]
            },
            {
                "args": [[5, 25, 75], 100],
                "kwargs": {},
                "expect": [2, 3]
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().twoSum(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
