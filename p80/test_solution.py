from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[1, 1, 1, 2, 2, 3]],
                "kwargs": {},
                "expect": (5, [1, 1, 2, 2, 3]),
            },
            {
                "args": [[0, 0, 1, 1, 1, 1, 2, 3, 3]],
                "kwargs": {},
                "expect": (7, [0, 0, 1, 1, 2, 3, 3]),
            },

        ]
        for index, case in enumerate(cases, start=1):
            inp = case["args"][0]
            result = Solution().removeDuplicates(*case["args"], **case["kwargs"])
            expect, expect_inp = case["expect"]
            self.assertEqual(inp[:result], expect_inp, f"case {index} failed")
