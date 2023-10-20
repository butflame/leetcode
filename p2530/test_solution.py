from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[10, 10, 10, 10, 10], 5],
                "kwargs": {},
                "expect": 50
            },
            {
                "args": [[1, 10, 3, 3, 3], 3],
                "kwargs": {},
                "expect": 17
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().maxKelements(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
