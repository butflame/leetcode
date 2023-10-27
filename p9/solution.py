class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 骚操作，反转后一半数字
        # 先处理边界情况：
        #   1. 负数不可能
        #   2. 除0以外以0结尾的不可能

        if x < 0:
            return False
        elif x == 0:
            return True
        elif x % 10 == 0:
            return False

        # 开始反转数字
        tmp = 0
        while tmp < x:
            tmp = tmp * 10 + x % 10
            x = x // 10
        # 两种情况：
        # - 偶数位数字 12344321, 反转后的结果为1234 1234
        # - 奇数位数字 1234321, 反转后的结果为 123 4321
        return x == tmp or x == tmp // 10
