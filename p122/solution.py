# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(1, len(prices)):
            ret += max(0, prices[i] - prices[i - 1])
        return ret
