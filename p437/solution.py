from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def root_sum(root, target):
            # 由root开始的路径
            if not root:
                return 0
            ret = 1 if root.val == target else 0
            next_target = target - root.val
            ret += root_sum(root.left, next_target)
            ret += root_sum(root.right, next_target)
            return ret

        if not root:
            return 0
        ret = root_sum(root, targetSum)
        ret += self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        return ret
