from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ret = 0
        masks = []
        for word in words:
            current_mask = 0
            for char in word:
                current_mask |= 1 << (ord(char) - ord('a'))
            masks.append(current_mask)

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j]:
                    continue

                ret = max(ret, len(words[i]) * len(words[j]))

        return ret
