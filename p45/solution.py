# https://leetcode.cn/problems/jump-game-ii/description/
from typing import List


def max_index(nums: List[int]) -> int:
    ret = 0
    current_max = nums[ret]
    for i in range(len(nums)):
        if nums[i] + i > current_max:
            current_max = nums[i] + i
            ret = i
    return ret


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        i = 0
        while i < len(nums) - 1:
            current_value = nums[i]
            can_reach_max_index = i + current_value
            if can_reach_max_index >= len(nums) - 1:
                step += 1
                break
            can_reach = nums[i + 1: can_reach_max_index + 1]
            current_choice = max_index(can_reach) + 1
            i += current_choice
            step += 1

        return step
