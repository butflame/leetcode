from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product2elements = {}
        for index_a in range(len(nums)):
            for index_b in (range(index_a + 1, len(nums))):
                product = nums[index_a] * nums[index_b]
                product2elements.setdefault(product, 0)
                product2elements[product] += 1
        ret = 0
        for k, v in product2elements.items():
            ret += v * (v - 1) * 4
        return ret
