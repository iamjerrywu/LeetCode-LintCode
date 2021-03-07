"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        self.find_most_left(root)
    """
    @return: True if there has next node, or false
    """
    # left minumum path
    def find_most_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left    
    
    def hasNext(self):
        # write your code here
        return len(self.stack) > 0
    """
    @return: return next node
    """
    def _next(self):
        # write your code here
        node = self.stack.pop()
        if node.right:
            self.find_most_left(node.right)
        return node