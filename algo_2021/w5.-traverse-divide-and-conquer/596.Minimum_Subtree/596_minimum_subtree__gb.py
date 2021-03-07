"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def __init__(self):
        self.minimum_weight = float('inf')
        self.minimum_subtree_root = None
    
    def findSubtree(self, root):
        # write your code here
        self.get_tree_sum(root)
        return self.minimum_subtree_root
    
    def get_tree_sum(self, root):
        if root is None:
            return 0
        
        left_weight = self.get_tree_sum(root.left)
        right_weight = self.get_tree_sum(root.right)
        root_weight = left_weight + right_weight + root.val
        
        if root_weight < self.minimum_weight:
            self.minimum_subtree_root = root
            self.minimum_weight = root_weight
        return root_weight