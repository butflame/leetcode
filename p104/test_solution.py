from typing import List, Optional
from unittest import TestCase

from .solution import Solution, TreeNode


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [build_tree([3, 9, 20, None, None, 15, 7])],
                "kwargs": {},
                "expect": 3
            },
            {
                "args": [build_tree([1, None, 2])],
                "kwargs": {},
                "expect": 2
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().maxDepth(*case["args"], **case["kwargs"])
            expect = case["expect"]
            self.assertEqual(result, expect, f"case {index} failed")


def build_tree(nums: List[int], pos=0) -> Optional[TreeNode]:
    if pos >= len(nums):
        return None
    if nums[pos] is None:
        return None
    return TreeNode(
        nums[pos],
        build_tree(nums, 2 * pos + 1),
        build_tree(nums, 2 * pos + 2),
    )
