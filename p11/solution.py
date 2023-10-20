from typing import List

"""
只需要从两遍往中间靠，并不需要双重循环，因为：
假设左右两边的值为x, y，其间距为t，那么面积s为
    s = (min(x, y)) * t
此时，假设x<=y，那么min(x,y)=x，即：
- c1: 若此时选择移动y对应的下标，更改y的值为y2，min(x,y2)的值不可能大于x
- c2: 若此时选择移动x对应的下标，更改x的值为x2，min(x2,y)的值有可能大于x
同时因为每次移动，t都会变更为t-1, 即：
- c1所导致的s的新值s2必然满足 s2 <= s
- c2所导致的s的新值s2可能满足：s2 <= s 或 s2 > s
显然，每次仅移动值较小的下标即可满足本题的诉求
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        the_max = 0
        low, high = 0, len(height) - 1
        while low < high:
            the_current = abs(low - high) * min(height[low], height[high])
            the_max = max(the_current, the_max)
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return the_max
