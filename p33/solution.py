"""
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

提示：

1 <= nums.length <= 5000
-10**4 <= nums[i] <= 10**4
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-10**4 <= target <= 10**4
"""
from typing import List
from unittest import TestCase


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分找旋转位置，再二分找目标值
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        rotate_idx = self.bin_search_rotate_idx(nums)
        found_in_left = self.bin_search(nums, target, 0, rotate_idx - 1)
        found_in_right = self.bin_search(nums, target, rotate_idx, len(nums) - 1)
        if found_in_left != -1:
            return found_in_left
        return found_in_right

    def bin_search(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def bin_search_rotate_idx(self, nums):
        if len(nums) <= 1:
            return 0
        pivot = nums[0]
        left, right = 1, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > pivot:
                left = mid + 1
            else:
                pivot = nums[mid]
                right = mid - 1
        return left


class TestSolution(TestCase):
    def test_solution(self):
        s = Solution()
        cases = [
            {
                "input": [[4, 5, 6, 7, 0, 1, 2], 0],
                "expect": 4
            },
            {
                "input": [[4, 5, 6, 7, 0, 1, 2], 3],
                "expect": -1
            },
            {
                "input": [[7, 0, 1, 2, 3, 4, 5, 6], 3],
                "expect": 4
            },
            {
                "input": [[1], 0],
                "expect": -1
            },
        ]
        for idx, c in enumerate(cases, start=1):
            expect_ = c["expect"]
            i = s.search(*c["input"])
            self.assertEqual(expect_, i, f"fail on {idx}")

    def test_bin_search_rotate_idx(self):
        s = Solution()
        cases = [
            {
                "input": [[4, 5, 6, 7, 0, 1, 2]],
                "expect": 4
            },
            {
                "input": [[7, 0, 1, 2, 3, 4, 5, 6]],
                "expect": 1
            },
            {
                "input": [[1]],
                "expect": 0
            },
            {
                "input": [[2, 1]],
                "expect": 1
            },

        ]
        for idx, c in enumerate(cases, start=1):
            expect_ = c["expect"]
            rotate_idx = s.bin_search_rotate_idx(*c["input"])
            self.assertEqual(expect_, rotate_idx, f"fail on {idx}")
