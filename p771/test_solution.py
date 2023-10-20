from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["aA", "aAAbbbb"],
                "kwargs": {},
                "expect": 3
            },
            {
                "args": ["z", "ZZ"],
                "kwargs": {},
                "expect": False
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().numJewelsInStones(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
