from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ret = 0
        for i in range(left, right + 1):
            if words[i][0] in ['a', 'e', 'i', 'o', 'u'] and words[i][-1] in ['a', 'e', 'i', 'o', 'u']:
                ret += 1
        return ret
