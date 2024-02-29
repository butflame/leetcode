"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

提示：

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成

"""
from typing import List
from unittest import TestCase


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        seen = set()
        tmp = []
        exists = []

        def bt(row, col):
            if not (0 <= row < m and 0 <= col < n):
                return
            if (row, col) in seen:
                return
            next_idx = len(tmp)
            current_char = board[row][col]
            if current_char == word[next_idx]:
                if next_idx == len(word) - 1:
                    exists.append(1)
                    return
                else:
                    tmp.append(word[next_idx])
                    seen.add((row, col))
                    bt(row, col + 1)
                    bt(row, col - 1)
                    bt(row + 1, col)
                    bt(row - 1, col)
                    seen.remove((row, col))
                    tmp.pop()
        for i in range(m):
            for j in range(n):
                bt(i, j)
        return bool(exists)


class TestSolution(TestCase):
    def test_generateParenthesis(self):
        s = Solution()
        cases = [
            {
                "input": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"],
                "expect": True,
            },
            {
                "input": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"],
                "expect": True,
            },
            {
                "input": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"],
                "expect": False,
            },
            {
                "input": [[["b"], ["a"], ["b"], ["b"], ["a"]], "bba"],
                "expect": False,
            },
            {
                "input": [[["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"],
                "expect": True,
            },
        ]
        for idx, c in enumerate(cases, start=1):
            expect_ = c["expect"]
            rotate_idx = s.exist(*c["input"])
            self.assertEqual(expect_, rotate_idx, f"fail on {idx}")
