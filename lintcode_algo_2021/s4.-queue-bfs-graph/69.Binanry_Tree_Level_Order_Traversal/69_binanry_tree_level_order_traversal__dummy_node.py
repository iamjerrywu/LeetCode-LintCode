"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from queue import Queue
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
        
        queue = collections.deque([root, None])
        res, level = [], []
        while queue:
            node = queue.popleft()
            if node is None:
                res.append(level)
                # update level
                level = []
                if queue:
                    # means still have next layer
                    # need to assign None in end of layer
                    queue.append(None)
                continue
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
