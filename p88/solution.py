# https://leetcode.cn/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        index1, index2 = m - 1, n - 1
        tail = m + n - 1
        while index1 >= 0 or index2 >= 0:
            if index1 < 0:
                nums1[tail] = nums2[index2]
                index2 -= 1
            elif index2 < 0:
                nums1[tail] = nums1[index1]
                index1 -= 1
            elif nums1[index1] > nums2[index2]:
                nums1[tail] = nums1[index1]
                index1 -= 1
            else:
                nums1[tail] = nums2[index2]
                index2 -= 1

            tail -= 1
