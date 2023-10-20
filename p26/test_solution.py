from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[1, 1, 2]],
                "kwargs": {},
                "expect": 2
            },
            {
                "args": [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]],
                "kwargs": {},
                "expect": 5
            },

        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().removeDuplicates(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
