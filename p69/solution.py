class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            tmp = mid ** 2
            if tmp > x:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        return ans
