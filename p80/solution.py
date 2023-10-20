# https://leetcode.cn/problems/remove-element/description/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i, j = 1, 2
        while i < len(nums) and j < len(nums):
            if nums[j] == nums[i]:
                if nums[i] != nums[i - 1]:
                    nums[i + 1] = nums[j]
                    i += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
            j += 1
        return i + 1
