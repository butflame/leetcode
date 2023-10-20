from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
                "kwargs": {},
                "expect": [1, 2, 2, 3, 5, 6],
            },
            {
                "args": [[1], 1, [], 0],
                "kwargs": {},
                "expect": [1],
            },
            {
                "args": [[0], 0, [1], 1],
                "kwargs": {},
                "expect": [1],
            },

        ]
        for index, case in enumerate(cases, start=1):
            inp = case["args"][0]
            Solution().merge(*case["args"], **case["kwargs"])
            expect_inp = case["expect"]
            self.assertEqual(inp, expect_inp, f"case {index} failed")
