from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        ret = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                ret += 1
            else:
                break
        return ret
