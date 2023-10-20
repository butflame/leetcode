from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[5, 19, 8, 1]],
                "kwargs": {},
                "expect": 3
            },
            {
                "args": [[3, 8, 20]],
                "kwargs": {},
                "expect": 3
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().halveArray(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
