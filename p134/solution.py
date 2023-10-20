# https://leetcode.cn/problems/gas-station/
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        remain = [gas[i] - cost[i] for i in range(n)]

        start = 0
        while start < n:
            current_total = 0
            step = 0
            while step < n:
                current_total += remain[(start + step) % n]
                if current_total < 0:
                    break
                step += 1
            if step == n:
                return start
            else:
                start += step + 1
        return -1
