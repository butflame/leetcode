# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.__class__.__name__}> val: {self.val}, left: {self.left}, right: {self.right}"


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, root)

    def check(self, a: Optional[TreeNode], b: Optional[TreeNode]):
        if not a and not b:
            return True
        elif not a or not b:
            return False
        return a.val == b.val and self.check(a.left, b.right) and self.check(a.right, b.left)
