from unittest import TestCase

from .solution import Solution


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": ["/home/"],
                "kwargs": {},
                "expect": "/home"
            },
            {
                "args": ["/../"],
                "kwargs": {},
                "expect": "/"
            },
            {
                "args": ["/home//foo/"],
                "kwargs": {},
                "expect": "/home/foo"
            },
            {
                "args": ["/a/./b/../../c/"],
                "kwargs": {},
                "expect": "/c"
            },
            {
                "args": ["/a//b////c/d//././/.."],
                "kwargs": {},
                "expect": "/a/b/c"
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().simplifyPath(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(expect, result, f"case {index} failed")
