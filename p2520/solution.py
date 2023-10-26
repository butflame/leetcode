class Solution:
    def countDigits(self, num: int) -> int:
        ret = 0
        tmp = num
        while tmp:
            tail = tmp % 10
            tmp = tmp // 10
            if num % tail == 0:
                ret += 1
        return ret
