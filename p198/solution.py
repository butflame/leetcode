from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        有数组f，以f[k]代表数组nums[0:k+1]的答案
        则有：
        - len(nums) <= 2时，答案为max(nums)
        - len(nums) > 2时，2 <= k <= len(nums) - 1 满足方程 f[k] = max(f[k-1], f[k-2] + nums[k])
        """
        if len(nums) <= 2:
            return max(nums)
        i, j = nums[0], max(nums[0:2])
        for k in range(2, len(nums)):
            i, j = j, max(i+nums[k], j)
        return j
