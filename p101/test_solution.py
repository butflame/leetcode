from typing import List, Optional
from unittest import TestCase

from .solution import Solution, TreeNode


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [build_tree([1, 2, 2, 3, 4, 4, 3])],
                "kwargs": {},
                "expect": True
            },
            {
                "args": [build_tree([1, 2, 2, None, 3, None, 3])],
                "kwargs": {},
                "expect": False
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().isSymmetric(*case["args"], **case["kwargs"])
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
