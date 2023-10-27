# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.__class__.__name__}> val: {self.val}, left: {self.left}, right: {self.right}"

    def __eq__(self, other):
        if not other or not isinstance(other, self.__class__):
            return False

        return self.val == other.val and self.left == other.left and self.right == other.right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
