from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[1, 2, 3, 4, 5, 6, 7], 3],
                "kwargs": {},
                "expect": [5, 6, 7, 1, 2, 3, 4]
            },
            {
                "args": [[-1, -100, 3, 99], 2],
                "kwargs": {},
                "expect": [3, 99, -1, -100]
            },
        ]
        for index, case in enumerate(cases, start=1):
            inp = case["args"][0]
            Solution().rotate(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(inp, expect, f"case {index} failed")
