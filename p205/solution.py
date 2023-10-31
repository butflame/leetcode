class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        tmp = {}
        tmp_r = {}
        for i in range(len(s)):
            x, y = s[i], t[i]
            exists_y = tmp.get(x)
            if exists_y and exists_y != y:
                return False
            exists_x = tmp_r.get(y)
            if exists_x and exists_x != x:
                return False
            tmp.setdefault(x, y)
            tmp_r.setdefault(y, x)
        return True
