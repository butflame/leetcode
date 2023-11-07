from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [["are","amy","u"], 0, 2],
                "kwargs": {},
                "expect": 2,
            },
            {
                "args": [["hey","aeo","mu","ooo","artro"], 1, 4],
                "kwargs": {},
                "expect": 3
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().vowelStrings(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
