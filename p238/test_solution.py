from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[1, 2, 3, 4]],
                "kwargs": {},
                "expect": [24, 12, 8, 6]
            },
            {
                "args": [[-1, 1, 0, -3, 3]],
                "kwargs": {},
                "expect": [0, 0, 9, 0, 0]
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().productExceptSelf(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
