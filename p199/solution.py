from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 左/右视图，层序遍历取每层的左/右
        if not root:
            return []
        q = [root]
        ret = []
        pushed_times = 1
        while q:
            ret.append(q[0].val)
            current_pushed_times = 0
            for _ in range(pushed_times):
                node = q.pop(0)
                if node.right:
                    q.append(node.right)
                    current_pushed_times += 1
                if node.left:
                    q.append(node.left)
                    current_pushed_times += 1
            pushed_times = current_pushed_times
        return ret




