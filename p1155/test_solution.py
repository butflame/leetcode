from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    cases = [
        {
            "args": [1, 6, 3],
            "kwargs": {},
            "expect": 1
        },
        {
            "args": [2, 6, 7],
            "kwargs": {},
            "expect": 6
        },
        {
            "args": [3, 6, 15],
            "kwargs": {},
            "expect": 10
        },
        {
            "args": [2, 6, 6],
            "kwargs": {},
            "expect": 5
        },
        {
            "args": [3, 6, 12],
            "kwargs": {},
            "expect": 25
        },
        {
            "args": [3, 6, 13],
            "kwargs": {},
            "expect": 21
        },
        {
            "args": [3, 6, 14],
            "kwargs": {},
            "expect": 15
        },
        {
            "args": [3, 6, 15],
            "kwargs": {},
            "expect": 10
        },
        {
            "args": [3, 6, 16],
            "kwargs": {},
            "expect": 6
        },
        {
            "args": [3, 6, 17],
            "kwargs": {},
            "expect": 3
        },
        {
            "args": [4, 6, 18],
            "kwargs": {},
            "expect": 80
        },
        {
            "args": [4, 6, 15],
            "kwargs": {},
            "expect": 140
        },
        {
            "args": [5, 6, 20],
            "kwargs": {},
            "expect": 651
        },
        {
            "args": [30, 30, 500],
            "kwargs": {},
            "expect": 222616187
        },
        {
            "args": [8, 8, 32],
            "kwargs": {},
            "expect": 848443
        },
        {
            "args": [6, 6, 18],
            "kwargs": {},
            "expect": 3431
        },
        {
            "args": [15, 15, 113],
            "kwargs": {},
            "expect": 881935240
        },
        {
            "args": [2, 10, 6],
            "kwargs": {},
            "expect": 5
        },
    ]

    def test_it(self):
        for index, case in enumerate(self.cases, start=1):
            result = Solution().numRollsToTarget(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")

    def test_it2(self):
        for index, case in enumerate(self.cases, start=1):
            result = Solution().numRollsToTarget2(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")

    def test_it3(self):
        for index, case in enumerate(self.cases, start=1):
            result = Solution().numRollsToTarget3(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")

    def test_it32(self):
        for index, case in enumerate(self.cases, start=1):
            result = Solution().numRollsToTarget32(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")

    def test_it4(self):
        for index, case in enumerate(self.cases, start=1):
            result = Solution().numRollsToTarget4(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
