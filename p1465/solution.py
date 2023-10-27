from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        verticalCuts.sort()
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        max_v = 0
        max_h = 0
        for i in range(len(horizontalCuts) - 1):
            max_h = max(max_h, horizontalCuts[i + 1] - horizontalCuts[i])
        for i in range(len(verticalCuts) - 1):
            max_v = max(max_v, verticalCuts[i + 1] - verticalCuts[i])

        mod = 10 ** 9 + 7
        return (max_h * max_v) % mod
