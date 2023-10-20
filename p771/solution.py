class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ret = 0
        tmp = set(jewels)
        for i in stones:
            if i in tmp:
                ret += 1
        return ret
