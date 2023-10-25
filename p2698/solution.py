class Solution:
    def punishmentNumber(self, n: int) -> int:
        ret = 0
        for i in range(1, n+1):
            tmp = i * i
            if self.ok(str(tmp), 0, i):
                ret += tmp
        return ret

    def ok(self, k: str, pos: int, target: int):
        if pos >= len(k):
            return target == 0

        current = 0
        for i in range(pos, len(k)):
            current = current * 10 + int(k[i])
            if target - current < 0:
                return False
            if self.ok(k, i+1, target - current):
                return True
        return False
