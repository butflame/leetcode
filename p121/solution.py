# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for p in prices:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)
        return max_profit
