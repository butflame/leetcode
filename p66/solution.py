from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = []
        plus = 1
        i = len(digits) - 1
        while i >= 0:
            current = digits[i] + plus
            plus = current // 10
            ret.insert(0, current % 10)
            i -= 1
        if plus:
            ret.insert(0, plus)
        return ret
