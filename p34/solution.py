"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。


"""
from typing import List
from unittest import TestCase


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left_idx = self.bin_search(nums, target)
        right_idx = self.bin_search(nums, target, False) - 1
        ret = [-1, -1]
        if 0 <= left_idx < len(nums) and nums[left_idx] == target:
            ret[0] = left_idx
        if 0 <= right_idx < len(nums) and nums[right_idx] == target:
            ret[1] = right_idx
        return ret

    def bin_search(self, arr, i, can_include=True):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if can_include:
                if arr[mid] >= i:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[mid] > i:
                    right = mid - 1
                else:
                    left = mid + 1
        return left


class TestSolution(TestCase):
    def test_solution(self):
        s = Solution()
        cases = [
            {
                "input": [[5, 7, 7, 8, 8, 10], 8],
                "expect": [3, 4]
            },
            {
                "input": [[5, 7, 7, 8, 8, 10], 6],
                "expect": [-1, -1]
            },
            {
                "input": [[], 0],
                "expect": [-1, -1]
            },
        ]
        for c in cases:
            self.assertListEqual(c["expect"], s.searchRange(*c["input"]))
