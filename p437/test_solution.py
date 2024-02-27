from unittest import TestCase
from .solution import TreeNode, Solution


class TestMy(TestCase):
    def test_solution(self):
        n1 = TreeNode(val=3, left=TreeNode(val=3), right=TreeNode(val=-2))
        n2 = TreeNode(val=2, right=TreeNode(val=1))
        n3 = TreeNode(val=5, left=n1, right=n2)
        n4 = TreeNode(val=-3, right=TreeNode(val=11))
        root = TreeNode(val=10, left=n3, right=n4)

        s = Solution()
        self.assertEqual(3, s.pathSum(root, 8))
