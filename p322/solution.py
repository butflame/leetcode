from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        数组f, f[i]表示按照给定的coins组成总额i所需的最小硬币数
        则对于任意i, 有 f[i] = min([f[i - v]  for v in coins]) + 1
        """
        if amount == 0:
            return 0
        f = [-1] * amount
        f.insert(0, 0)
        for v in coins:
            if v >= len(f):
                continue
            f[v] = 1

        for i in range(amount):
            current_min = None
            for v in coins:
                if i + 1 - v < 0:
                    continue
                last = f[i + 1 - v]
                if last == -1:
                    continue
                if current_min is None:
                    current_min = last + 1
                else:
                    current_min = min(current_min, last + 1)
            if current_min is not None:
                f[i + 1] = current_min
        return f[-1]

