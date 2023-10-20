# https://leetcode.cn/problems/remove-element/description/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        valid_index, invalid_index = 0, len(nums) - 1
        while valid_index <= invalid_index:
            if nums[valid_index] != val:
                valid_index += 1
            else:
                nums[valid_index], nums[invalid_index] = nums[invalid_index], nums[valid_index]
                invalid_index -= 1

        return valid_index
