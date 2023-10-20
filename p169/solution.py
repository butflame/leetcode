# https://leetcode.cn/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = None
        pivot = 0
        for i in nums:
            if current is None:
                current = i
                pivot += 1
            else:
                if i == current:
                    pivot += 1
                else:
                    pivot -= 1
                    if pivot <= 0:
                        current = None
        return current
