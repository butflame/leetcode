from dataclasses import dataclass
from typing import List


class Stack(list):
    def pop(self):
        return super().pop()

    def push(self, v):
        self.append(v)

    def top(self):
        return self[-1]


@dataclass
class Point:
    x: int
    y: int


class Solution:
    def trap(self, height: List[int]) -> int:
        # 题解1 其称之为动态规划，其实就是双向扫描
        if not height:
            return 0
        n = len(height)
        current_left_max = 0
        max_array = []
        ret = 0
        for i in range(n):
            current_left_max = max(height[i], current_left_max)
            max_array.append(current_left_max)

        current_right_max = 0
        for i in range(n):
            v = n - 1 - i
            current_right_max = max(height[v], current_right_max)
            max_array[v] = min(max_array[v], current_right_max)
            volume = max_array[v] - height[v]
            ret += volume

        return ret

    def trap2(self, height: List[int]) -> int:
        # 题解2 单调栈
        """
        核心思路：
        积累雨水可以形象的理解为从左至右爬山，对于雨水来说，每次下坡都在「积蓄势能」，而每逢上坡至高度h，则可以兑现此前积累的不超过h的势能
        以 [0, 1, 2, 3, 2, 1, 2, 4]举例
        s1: 0->1->2->3的过程为上坡，但此前没有积蓄的势能
        s2: 3->2->1的过程分两次各积累了高度为1的势能
        s3: 再次上坡1->2的过程应兑现此前积累的不超过h的势能，因此仅可对兑现上一步中2->1的部分势能，3->2部分积累的势能保留
        s4: 2->4的过程则可以兑现s2中3->2积累的势能

        容易发现，每次兑换势能时，会倒序追溯此前下坡的过程，因此很适合用栈来实现
        """

        ret = 0
        stack = Stack()

        for x, y in enumerate(height):
            while stack and y > stack.top().y:
                # 每次遇到比栈顶更高的元素则弹空栈
                # 若当前栈不空 且 当前高度大于栈顶高度
                # 弹出栈顶
                top = stack.pop()
                # 如果此时栈空，代表栈顶所代表的元素左边没有元素/不比他高，结束while循环
                if not stack:
                    break
                # 访问目前的栈顶，即再上一个元素
                left = stack.top()
                # 取当前宽度
                tmp_width = x - left.x - 1
                # 取最小高度
                tmp_height = min(left.y, y) - top.y
                ret += tmp_width * tmp_height
            stack.append(Point(x, y))

        return ret

    def trap3(self, height: List[int]) -> int:
        max_left = max_right = 0
        left, right = 0, len(height) - 1
        ret = 0
        while left < right:
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)

            if height[left] < height[right]:
                ret += max_left - height[left]
                left += 1
            else:
                ret += max_right - height[right]
                right -= 1

        return ret
