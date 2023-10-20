from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]],
                "kwargs": {},
                "expect": 3
            },
            {
                "args": [[2, 3, 4], [3, 4, 3]],
                "kwargs": {},
                "expect": -1
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().canCompleteCircuit(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
