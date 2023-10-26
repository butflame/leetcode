from typing import List, Optional
from unittest import TestCase

from .solution import Solution, TreeNode


class Test(TestCase):
    def test_it(self):
        cases = [
            {
                "args": [build_tree([4, 2, 7, 1, 3, 6, 9])],
                "kwargs": {},
                "expect": build_tree([4, 7, 2, 9, 6, 3, 1])
            },
            {
                "args": [build_tree([2, 1, 3])],
                "kwargs": {},
                "expect": build_tree([2, 3, 1])
            },
            {
                "args": [build_tree([])],
                "kwargs": {},
                "expect": build_tree([])
            },
        ]
        for index, case in enumerate(cases, start=1):
            result = Solution().invertTree(*case["args"], **case["kwargs"])
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
