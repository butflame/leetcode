from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]],
                "kwargs": {},
                "expect": 6
            },
            {
                "args": [[4, 2, 0, 3, 2, 5]],
                "kwargs": {},
                "expect": 9
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().trap(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
            result = Solution().trap2(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
            result = Solution().trap3(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
