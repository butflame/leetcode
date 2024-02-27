from unittest import TestCase
from .solution import Solution


class TestSolution(TestCase):
    def test_solution(self):
        cases = [
            {
                "input": [1, 2, 3],
                "expect": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            },
        ]
        s = Solution()
        for c in cases:
            self.assertEqual(c["expect"], s.permute(c["input"]))
