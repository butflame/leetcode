from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[2, 3, 1, 1, 4]],
                "kwargs": {},
                "expect": 2
            },
            {
                "args": [[2, 3, 0, 1, 4]],
                "kwargs": {},
                "expect": 2
            },

        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().jump(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
