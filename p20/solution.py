# https://leetcode.cn/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        tmp = []
        for i in s:
            if i in "[{(":
                tmp.append(i)
            elif i in "])}":
                if not tmp:
                    return False
                last = tmp.pop()
                if i == "]" and last != "[":
                    return False
                if i == ")" and last != "(":
                    return False
                if i == "}" and last != "{":
                    return False
        return not tmp
