from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            the_sum = numbers[low] + numbers[high]
            if the_sum == target:
                return [low + 1, high + 1]
            elif the_sum > target:
                high -= 1
            else:
                low += 1
