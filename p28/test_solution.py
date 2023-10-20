from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[3, 2, 2, 3], 3],
                "kwargs": {},
                "expect": (2, [2, 2]),
            },
            {
                "args": [[0, 1, 2, 2, 3, 0, 4, 2], 2],
                "kwargs": {},
                "expect": (5, [0, 1, 4, 0, 3]),
            },

        ]
        for index, case in enumerate(cases, start=1):
            inp = case["args"][0]
            result = Solution().removeElement(*case["args"], **case["kwargs"])
            expect, expect_inp = case["expect"]
            self.assertEqual(inp[:result], expect_inp, f"case {index} failed")
