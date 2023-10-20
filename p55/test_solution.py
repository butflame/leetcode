from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[2, 3, 1, 1, 4]],
                "kwargs": {},
                "expect": True
            },
            {
                "args": [[3, 2, 1, 0, 4]],
                "kwargs": {},
                "expect": False
            },

        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().canJump(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
