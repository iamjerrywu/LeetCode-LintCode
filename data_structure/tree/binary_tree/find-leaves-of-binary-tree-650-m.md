# Find Leaves of Binary Tree 650 \(M\)

## Problem

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.Example

**Example1**  
Input: {1,2,3,4,5}  
Output: `[[4, 5, 3], [2], [1]]`.  
Explanation:

```text
    1
   / \
  2   3
 / \     
4   5    
```

**Example2**  
Input: {1,2,3,4}  
Output: `[[4, 3], [2], [1]]`.  
Explanation:

```text
    1
   / \
  2   3
 /
4 
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    # recurison def
    def add_to_lists(self, lists, curr_level, value):
        if curr_level == len(lists):
            lists.append([])
            
        lists[curr_level].append(value)
            
    
    def dfs(self, node, lists):
        # recursion termination
        if not node:
            # return -1, as root node, then it's level as 0 (lists[0])
            return -1
        
        #post order traversal
        left_level = self.dfs(node.left, lists)
        right_level = self.dfs(node.right, lists)
        
        curr_level = max(left_level, right_level) + 1
        self.add_to_lists(lists, curr_level, node.val)
        
        return curr_level
        
    def findLeaves(self, root):
        # write your code here
        lists = []
        if not root:
            return lists
        
        # post-order traverse, first left -> right -> node
        self.dfs(root, lists)
        return lists
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

