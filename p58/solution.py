class Solution:
    def lengthOfLastWord2(self, s: str) -> int:
        ret = 0
        last_is_space = True
        for i in s:
            if i.isspace():
                last_is_space = True
                continue
            if last_is_space:
                ret = 1
                last_is_space = False
            else:
                ret += 1

        return ret

    def lengthOfLastWord(self, s: str) -> int:
        ret = 0
        for i in s[::-1]:
            if i.isspace():
                if ret == 0:
                    continue
                else:
                    break
            ret += 1
        return ret
