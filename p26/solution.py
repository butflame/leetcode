# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
        return i + 1
