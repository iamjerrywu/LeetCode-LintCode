"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    # divide conquer solution 
    def binaryTreePaths(self, root):
        # write your code here
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            return [str(root.val)]
        for path in self.binaryTreePaths(root.left):
            res.append(str(root.val) + '->' + path)
        for path in self.binaryTreePaths(root.right):
            res.append(str(root.val) + '->' + path)
        return res