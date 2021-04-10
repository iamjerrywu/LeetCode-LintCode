"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        is_balanced, _ = self.validate(root)
        return is_balanced
    
    def validate(self, root):
        # if empty tree, it's balanced and return heigh = 0
        if not root:
            return True, 0
        
        is_left_balanced, left_height = self.validate(root.left)
        is_right_balanced, right_height = self.validate(root.right)
        root_height = max(left_height, right_height) + 1

        if not is_left_balanced or not is_right_balanced: 
            return False, root_height
        if abs(left_height - right_height) > 1:
            return False, root_height
        return True, root_height
        
