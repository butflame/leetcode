"""
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

提示：

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
candidates 的所有元素 互不相同
1 <= target <= 40
"""
from typing import List
from unittest import TestCase


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        tmp = []
        ret = []

        def bt(left_sum, gte=None):
            if left_sum == 0:
                ret.append(tmp[:])
                return
            for c in candidates:
                if c > left_sum:
                    continue
                if gte is not None and c < gte:
                    continue
                tmp.append(c)
                bt(left_sum - c, gte=c)
                tmp.pop()

        bt(target)

        return ret


class TestSolution(TestCase):
    def test_findMedianSortedArrays(self):
        s = Solution()
        cases = [
            {
                "input": [[2, 3, 6, 7], 7],
                "expect": [[2, 2, 3], [7]],
            },
            {
                "input": [[2, 3, 5], 8],
                "expect": [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
            },
            {
                "input": [[2], 1],
                "expect": [],
            },
        ]
        for idx, c in enumerate(cases, start=1):
            expect_ = c["expect"]
            rotate_idx = s.combinationSum(*c["input"])
            self.assertListEqual(expect_, rotate_idx, f"fail on {idx}")
