from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
        解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
        """
        ret = []
        tmp = []
        n = len(nums)

        def backtrace(idx=0):
            if idx >= n:
                ret.append(tmp[:])
                return
            # 不选择当前元素
            backtrace(idx + 1)

            # 选择当前元素
            tmp.append(nums[idx])
            backtrace(idx + 1)
            tmp.pop()

        backtrace()
        return ret
