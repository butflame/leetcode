# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ret = -1
        if len(haystack) < len(needle):
            return ret

        i = 0
        while i < len(haystack):
            j = 0
            while j < len(needle):
                if i + j >= len(haystack):
                    break
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            else:
                return i
            i += 1

        return ret
