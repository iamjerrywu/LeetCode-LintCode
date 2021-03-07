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
    def findSubtree(self, root):
        # write your code here
        _, min_node, _ = self.helper(root)
        return min_node
    
    def helper(self, root):
        if not root:
            return float('inf'), None, 0
        
        left_min_weight, left_min_node, left_sum = self.helper(root.left)
        right_min_weight, right_min_node, right_sum = self.helper(root.right)
        cur_sum = left_sum + right_sum + root.val
        
        if left_min_weight == min(left_min_weight, right_min_weight, cur_sum):
            return left_min_weight, left_min_node, cur_sum
        if right_min_weight == min(left_min_weight, right_min_weight, cur_sum):
            return right_min_weight, right_min_node, cur_sum
        return cur_sum, root, cur_sum
