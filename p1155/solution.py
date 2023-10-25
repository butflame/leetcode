class Solution:
    def numRollsToTarget2(self, n: int, k: int, target: int) -> int:
        cache = {"0_0": 1}
        ret = self.doit(n, k, target, cache)
        return int(ret)

    def doit(self, n, k, target, cache):
        cache_key = f"{n}_{target}"

        if n * k < target:
            return 0
        if cache_key in cache:
            return cache[cache_key]
        # if n == 0:
        #     if target == 0:
        #         return 1
        #     return 0

        if n == 1:
            if 0 < target <= k:
                return 1
            return 0

        ret = 0
        for i in range(1, k + 1):
            tmp = self.doit(n - 1, k, target - i, cache)
            if tmp > 0:
                ret += tmp % (10 ** 9 + 7)
        ret = ret % (10 ** 9 + 7)
        cache[cache_key] = ret
        return ret

    """
    func(x,y)代表x个骰子、target为y的值, 则该问题一定满足以下方程：
        for i in [1..n]
          for j in [1..target]
            func(i, j) = func(i-1, j-1) + func(i-1, j-2) + ... + func(i-1, j-k)
    """

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        维护二维数组f, f[x][y] 即为 func(x, y)
        """

        mod = 10 ** 9 + 7
        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for dice_count in range(1, n + 1):
            for current_target in range(1, target + 1):
                for current_value in range(1, k + 1):
                    if current_target < current_value:
                        continue
                    f[dice_count][current_target] = f[dice_count][current_target] + f[dice_count - 1][current_target - current_value]
        return f[n][target] % mod

    def numRollsToTarget32(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        f = [1] + [0] * target  # 此时f代表0个骰子时的状态
        for dice_count in range(1, n + 1):
            g = [0] * (target + 1)
            for current_target in range(target + 1):
                for left_target in range(max(0, current_target - k), current_target):
                    g[current_target] = (g[current_target] + f[left_target]) % mod
            f = g  # 使用f维持dice_count个骰子时的状态，循环结束后即代表n个骰子的状态
        return f[target]

    def numRollsToTarget3(self, n: int, k: int, target: int) -> int:
        """
        仅使用两个数组，因方程
        func(i, j) = func(i-1, j-1) + func(i-1, j-2) + ... + func(i-1, j-k)
        可知，对任意j, func(i, j)的解仅需由func(i-1, j)的值求得
        因此当以i递增的顺序求解时，当有满足 0 < k <= n 的任意时刻我们仅需保持 k=i 及 k=i-1 的解，即可继续对k进行递增
        本例中，没轮循环时，以数组f表示func(i-1, j)，以数组g表示func(i, j)并对其进行求值
        当func(i, j)求值完成，func(i-1, j)即无需再保留，因此循环体结尾直接将数组g赋值于f，用以作为下一轮循环中的func(i-1, j)
        """
        mod = 10 ** 9 + 7
        f = [1] + [0] * target  # 此时f代表0个骰子时的状态
        for dice_count in range(1, n + 1):
            g = [0] * (target + 1)
            for current_target in range(target + 1):
                for current_value in range(1, k + 1):
                    if current_target < current_value:
                        break
                    left_target = current_target - current_value
                    # 此时f代表 dice_count - 1 个骰子时的状态
                    g[current_target] = (g[current_target] + f[left_target]) % mod
            f = g  # 使用f维持dice_count个骰子时的状态，循环结束后即代表n个骰子的状态
        return f[target]

    def numRollsToTarget4(self, n: int, k: int, target: int) -> int:
        """
        本例在numRollsToTarget3的基础上优化为仅使用一个数组f
        对数组f, 其中f[x][y]表示f(x, y)的解，在按照x递增,y递减的顺序求解时，上述的求解过程
            func(x, y) = func(x-1, y-k) + func(x-1, y-k+1) + ... func(x-1, y-1)
        中取值并无重叠，即当对x, y求解时
            下标idx 满足 0 <= idx <= y-1的部分表示骰子数i取值为x-1时的值
            下标idx 满足 y <= idx <= target的部分表示筛子数i取值为x时的值
        f的变化图示为：
            循环开始时
                f = [func(i-1, 0), func(i-1, 1), func(i-1, 2), ... func(i-1, j-2), func(i-1, j-1), func(i-1, j)]
            随着j的递减
                f = [func(i-1, 0), func(i-1, 1), func(i-1, 2), ... func(i-1, j-2), func(i-1, j-1), func(i  , j)]
                f = [func(i-1, 0), func(i-1, 1), func(i-1, 2), ... func(i-1, j-2), func(i  , j-1), func(i  , j)]
                f = [func(i-1, 0), func(i-1, 1), func(i-1, 2), ... func(i  , j-2), func(i  , j-1), func(i  , j)]
                ...
                f = [func(i-1, 0), func(i-1, 1), func(i  , 2), ... func(i  , j-2), func(i  , j-1), func(i  , j)]
                f = [func(i-1, 0), func(i  , 1), func(i  , 2), ... func(i  , j-2), func(i  , j-1), func(i  , j)]
                f = [func(i  , 0), func(i  , 1), func(i  , 2), ... func(i  , j-2), func(i  , j-1), func(i  , j)]
        """
        mod = 10 ** 9 + 7
        f = [1] + [0] * target  # 此时f代表0个骰子时的状态
        for dice_count in range(1, n + 1):
            for current_target in range(target, -1, -1):
                f[current_target] = 0
                for current_value in range(1, k + 1):
                    if current_target < current_value:
                        continue
                    f[current_target] = (f[current_target] + f[current_target - current_value]) % mod
        return f[target]
