class Solution:
    def climbStairs(self, n: int) -> int:
        """
        f(n) = f(n-1) + f(n-2)
        """
        if n <= 2:
            return n
        i, j = 1, 2
        for k in range(3, n+1):
            i, j = j, i+j
        return j
