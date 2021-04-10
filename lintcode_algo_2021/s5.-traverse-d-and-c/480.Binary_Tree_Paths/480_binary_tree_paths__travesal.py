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
    # travesal (DFS)
    def binaryTreePaths(self, root):
        # write your code here
        # result
        res = []
        if not root:
            res
        # put root node inside path
        path = [root]
        self.find_path(root, path, res)
        return res
    
    def find_path(self, node, path, res):
        if not node:
            return
        if not node.left and not node.right:
            res.append('->'.join([str(n.val) for n in path]))
            return res
        
        path.append(node.left)
        self.find_path(node.left, path, res)
        path.pop()

        path.append(node.right)
        self.find_path(node.right, path, res)
        path.pop()