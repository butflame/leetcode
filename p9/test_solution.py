from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            # {
            #     "args": [121],
            #     "kwargs": {},
            #     "expect": True
            # },
            # {
            #     "args": [-121],
            #     "kwargs": {},
            #     "expect": False
            # },
            # {
            #     "args": [10],
            #     "kwargs": {},
            #     "expect": False
            # },
            {
                "args": [1000021],
                "kwargs": {},
                "expect": False
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().isPalindrome(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")
