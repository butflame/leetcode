"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

提示：
1 <= s.length <= 16
s 仅由小写英文字母组成
"""
from collections import defaultdict
from typing import List
from unittest import TestCase


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        ret = list()
        ans = list()
        mem = defaultdict(lambda: False)

        def isPalindrome(i: int, j: int) -> int:
            if (i, j) not in mem:
                r = True
                while i <= j:
                    if s[i] != s[j]:
                        r = False
                        break
                    i += 1
                    j -= 1
                mem[(i, j)] = r
            return mem[(i, j)]

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if isPalindrome(i, j):
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()
        dfs(0)
        return ret


class TestSolution(TestCase):
    def test_partition(self):
        s = Solution()
        cases = [
            {
                "input": ["aab"],
                "expect": [["a", "a", "b"], ["aa", "b"]],
            },
            {
                "input": ["a"],
                "expect": [["a"]],
            },
        ]
        for idx, c in enumerate(cases, start=1):
            expect_ = c["expect"]
            rotate_idx = s.partition(*c["input"])
            self.assertEqual(expect_, rotate_idx, f"fail on {idx}")
