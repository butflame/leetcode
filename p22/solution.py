"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

提示：
1 <= n <= 8
"""
from typing import List
from unittest import TestCase


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        tmp = []
        ret = []
        lefts = []

        def bt(i=0):
            if i >= n * 2:
                ret.append("".join(tmp))
                return
            if n * 2 - i > len(lefts):
                tmp.append("(")
                lefts.append(0)
                bt(i+1)
                tmp.pop()
                lefts.pop()
            if len(lefts) > 0:
                tmp.append(")")
                lefts.pop()
                bt(i+1)
                lefts.append(0)
                tmp.pop()
        bt()
        return ret


class TestSolution(TestCase):
    def test_generateParenthesis(self):
        s = Solution()
        cases = [
            {
                "input": [3],
                "expect": ["((()))", "(()())", "(())()", "()(())", "()()()"],
            },
            {
                "input": [1],
                "expect": ["()"],
            },
        ]
        for idx, c in enumerate(cases, start=1):
            expect_ = c["expect"]
            rotate_idx = s.generateParenthesis(*c["input"])
            self.assertListEqual(expect_, rotate_idx, f"fail on {idx}")
