from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)


def reverse(l: List[int], start: int, end: int):
    while start < end:
        l[start], l[end] = l[end], l[start]
        start += 1
        end -= 1
