class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tmp = {}
        for i in range(len(s)):
            x, y = s[i], t[i]
            tmp.setdefault(x, 0)
            tmp.setdefault(y, 0)
            tmp[x] += 1
            tmp[y] -= 1
            if x in tmp and tmp[x] == 0:
                tmp.pop(x)
            if y in tmp and tmp[y] == 0:
                tmp.pop(y)
        return not tmp
