"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。
"""
from typing import List
from unittest import TestCase


# failed
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total_count = m + n
        odd = total_count % 2 == 1
        if odd:
            need_drop_cnt = total_count // 2
        else:
            need_drop_cnt = total_count // 2 - 1

        l1, r1, l2, r2 = 0, m - 1, 0, n - 1
        while l1 <= r1 and l2 <= r2 and need_drop_cnt > 0:
            mid1 = (l1 + r1) // 2
            mid2 = (l2 + r2) // 2
            v1, v2 = nums1[mid1], nums2[mid2]

            # 先试着扔小的
            if v1 <= v2:
                to_drop_count = mid1 - l1 + 1
            else:
                to_drop_count = mid2 - l2 + 1

            drop_less_nums = need_drop_cnt >= to_drop_count
            if drop_less_nums:
                if v1 < v2:
                    need_drop_cnt -= mid1 - l1 + 1
                    l1 = mid1 + 1
                elif v1 > v2:
                    need_drop_cnt -= mid2 - l2 + 1
                    l2 = mid2 + 1
                else:
                    if nums1[l1] < nums2[l2]:
                        need_drop_cnt -= mid1 - l1 + 1
                        l1 = mid1 + 1
                    else:
                        need_drop_cnt -= mid2 - l2 + 1
                        l2 = mid2 + 1
            else:
                if v1 > v2:
                    r1 = mid1 - 1
                elif v1 < v2:
                    r2 = mid2 - 1
                else:
                    if nums1[r1] < nums2[r2]:
                        r2 = mid2 - 1
                    else:
                        r1 = mid1 - 1

            tmp1 = nums1[l1:r1 + 1]
            tmp2 = nums2[l2:r2 + 1]
            print()

        if need_drop_cnt > 0:
            # 必有一个数组已空
            if l1 <= r1:
                l1 += need_drop_cnt
            else:
                l2 += need_drop_cnt
        if odd:
            if l1 <= r1 and l2 <= r2:
                return min(nums1[l1], nums2[l2])
            elif l1 <= r1:
                return nums1[l1]
            else:
                return nums2[l2]
        else:
            if l1 <= r1 and l2 <= r2:
                return (nums1[l1] + nums2[l2]) / 2.0
                # ret = 0
                # for i in range(2):
                #     if l1 <= r1 and l2 <= r2:
                #         if nums1[l1] < nums2[l2]:
                #             ret += nums1[l1]
                #             l1 += 1
                #         else:
                #             ret += nums2[l2]
                #             l2 += 1
                #     elif l1 <= r1:
                #         ret += nums1[l1]
                #         l1 += 1
                #     else:
                #         ret += nums2[l2]
                #         l2 += 1
                # return ret / 2.0
            elif l1 <= r1:
                return (nums1[l1] + nums1[l1 + 1]) / 2.0
            else:
                return (nums2[l2] + nums2[l2 + 1]) / 2.0


class TestSolution(TestCase):
    def test_findMedianSortedArrays(self):
        s = Solution()
        cases = [
            # {
            #     "input": [[1, 3], [2]],
            #     "expect": 2.0
            # },
            # {
            #     "input": [[1, 2], [3, 4]],
            #     "expect": 2.5
            # },
            # {
            #     "input": [[2, 2, 4, 4], [2, 2, 4, 4]],
            #     "expect": 3
            # },
            # {
            #     "input": [[1, 2, 3], [1, 2]],
            #     "expect": 2
            # },
            # {
            #     "input": [[1, 2], [1, 2, 3]],
            #     "expect": 2
            # },
            # {
            #     "input": [[0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1]],
            #     "expect": 0.0,
            # },
            # {
            #     "input": [[1, 2, 2], [1, 2, 3]],
            #     "expect": 2.0,
            # },
            {
                "input": [[1, 2], [-1, 3]],
                "expect": 1.5,
            },
        ]
        for idx, c in enumerate(cases, start=1):
            expect_ = c["expect"]
            rotate_idx = s.findMedianSortedArrays(*c["input"])
            self.assertEqual(expect_, rotate_idx, f"fail on {idx}")
