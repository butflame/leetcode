"""
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 中的所有整数 互不相同
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
"""
from typing import List
from unittest import TestCase


class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = nums[0]
        left, right = 1, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > pivot:
                left = mid + 1
            else:
                pivot = nums[mid]
                right = mid - 1
        if left >= len(nums):
            return nums[0]
        return nums[left]

class TestSolution(TestCase):
    def test_findMin(self):
        s = Solution()
        cases = [
            {
                "input": [[4, 5, 6, 7, 0, 1, 2]],
                "expect": 0
            },
            {
                "input": [[7, 0, 1, 2, 3, 4, 5, 6]],
                "expect": 0
            },
            {
                "input": [[1]],
                "expect": 1
            },
            {
                "input": [[3, 4, 5, 1, 2]],
                "expect": 1
            },
            {
                "input": [[11, 13, 15, 17]],
                "expect": 11
            },
            {
                "input": [[2, 1]],
                "expect": 1
            },
        ]
        for idx, c in enumerate(cases, start=1):
            expect_ = c["expect"]
            rotate_idx = s.findMin(*c["input"])
            self.assertEqual(expect_, rotate_idx, f"fail on {idx}")
