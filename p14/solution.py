# https://leetcode.cn/problems/longest-common-prefix/description/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                ret += chars[0]
            else:
                break
        return ret
