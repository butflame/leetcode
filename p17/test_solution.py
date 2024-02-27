from unittest import TestCase
from .solution import Solution


class TestSolution(TestCase):
    def test_solution(self):
        cases = [
            {
                "input": "23",
                "expect": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
            },
            {
                "input": "",
                "expect": [],
            },
            {
                "input": "2",
                "expect": ["a", "b", "c"],
            },
        ]
        s = Solution()
        for c in cases:
            self.assertEqual(c["expect"], s.letterCombinations(c["input"]), f"fail on {c['input']}")
