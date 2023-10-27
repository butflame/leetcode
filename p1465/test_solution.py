from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [5, 4, [1, 2, 4], [1, 3]],
                "kwargs": {},
                "expect": 4
            },
            {
                "args": [5, 4, [3, 1], [1]],
                "kwargs": {},
                "expect": 6
            },
            {
                "args": [5, 4, [3], [3]],
                "kwargs": {},
                "expect": 9
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().maxArea(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
