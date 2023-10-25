from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        建立数组f: List[bool]，f[k]表示s[0:k+1]是否可以由wordDict中的词表示
        为方便编码，在数组f中放入一额外元素f[0] = True
        则对任意k, 有f[k] = f[k - i] and s[k-i+1:k] in wordDict, 其中i为下标前移的步数
        """
        f = [False] * len(s)
        f.insert(0, True)
        for i in range(0, len(s)):
            for word in wordDict:
                if i - len(word) + 1 < 0:
                    continue
                current = s[i + 1 - len(word):i + 1]
                if current == word and f[i + 1 - len(word)]:
                    f[i + 1] = True
                    break
        return f[-1]
