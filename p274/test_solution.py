from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[3, 0, 6, 1, 5]],
                "kwargs": {},
                "expect": 3
            },
            {
                "args": [[1, 3, 1]],
                "kwargs": {},
                "expect": 1
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().hIndex(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
