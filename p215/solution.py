from typing import List
from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        tmp = []
        for i in nums:
            heappush(tmp, -i)
        for i in range(k):
            ret = heappop(tmp)
        return -ret
