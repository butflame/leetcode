from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [10],
                "kwargs": {},
                "expect": 182
            },
            {
                "args": [37],
                "kwargs": {},
                "expect": 1478
            },
            {
                "args": [45],
                "kwargs": {},
                "expect": 3503
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().punishmentNumber(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")

    def test_ok(self):
        cases = [
            {
                "args": ['1', 0, 1],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ['81', 0, 9],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ['100', 0, 1],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ['1296', 0, 36],
                "kwargs": {},
                "expect": True
            },
            {
                "args": ['2025', 0, 45],
                "kwargs": {},
                "expect": True
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().ok(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")

