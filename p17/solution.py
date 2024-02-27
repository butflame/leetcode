from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        """
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
        给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
        """
        ret = []
        if not digits:
            return ret
        tmp = []
        n = len(digits)

        def bt(idx=0):
            if idx >= n:
                ret.append("".join(tmp))
                return
            for i in m[digits[idx]]:
                tmp.append(i)
                bt(idx + 1)
                tmp.pop()

        bt()
        return ret
