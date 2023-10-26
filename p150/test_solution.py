from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            # {
            #     "args": [["2", "1", "+", "3", "*"]],
            #     "kwargs": {},
            #     "expect": 9
            # },
            # {
            #     "args": [["4", "13", "5", "/", "+"]],
            #     "kwargs": {},
            #     "expect": 6
            # },
            {
                "args": [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]],
                "kwargs": {},
                "expect": 22
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().evalRPN(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
