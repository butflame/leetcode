from heapq import heappush, heapreplace
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        heap = []
        n = len(nums)
        for i in range(n):
            heappush(heap, -nums[i])
        for i in range(k):
            num = -heap[0]
            if num == 1:
                return score + k - i
            score += num
            heapreplace(heap, -ceil(num / 3))
        return score
