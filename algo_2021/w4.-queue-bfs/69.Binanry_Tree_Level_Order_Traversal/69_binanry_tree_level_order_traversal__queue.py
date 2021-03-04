"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
        
        # step 1: put the first level into queue
        queue = collections.deque([root])
        res = []
        # step2: while queue not empty
        while queue:
            # step3: put every level (queue) value into result
            res.append([node.val for node in queue])
            # WARNING!
            # here don't need to write as size = len(queue), than range(size)..
            # since python the len(queue) would be parater for func range()
            # This make it the same as size = len(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
                
