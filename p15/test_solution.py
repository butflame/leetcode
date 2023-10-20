from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[-1, 0, 1, 2, -1, -4]],
                "kwargs": {},
                "expect": [[-1, -1, 2], [-1, 0, 1]]
            },
            {
                "args": [[0, 1, 1]],
                "kwargs": {},
                "expect": []
            },
            {
                "args": [[0, 0, 0]],
                "kwargs": {},
                "expect": [[0, 0, 0]]
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().threeSum(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
