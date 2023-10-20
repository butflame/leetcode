from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1]
        # product by left
        product_left = 1
        for i in range(1, len(nums)):
            product_left = product_left * nums[i - 1]
            ret.append(product_left)

        product_right = 1
        i = len(nums) - 2
        while i >= 0:
            product_right *= nums[i + 1]
            ret[i] *= product_right
            i -= 1

        return ret
