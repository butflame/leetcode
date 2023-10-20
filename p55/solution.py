# https://leetcode.cn/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach_max_index = 0
        max_index = len(nums) - 1
        for index, step in enumerate(nums):
            if index > can_reach_max_index:
                return False
            can_reach_max_index = max(can_reach_max_index, index + step)
            if can_reach_max_index >= max_index:
                return True
        return can_reach_max_index >= max_index
