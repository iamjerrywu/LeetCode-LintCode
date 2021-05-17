# Binary Tree Maximum Path Sum 94 \(M\)

## Problem

Given a binary tree, find the maximum path sum.  
The path may start and end at any node in the tree.  
\(Path sum is the sum of the weights of nodes on the path between two nodes.\)Example

**Example 1:**

Input:

```text
tree = {2}
```

Output:

```text
2
```

Explanation:

There is only one node 2  
**Example 2:**

Input:

```text
tree = {1,2,3}
```

Output:

```text
6
```

Explanation:

```text
As shown in the figure below, the longest path is 2-1-3
      1
     / \
    2   
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
    @param root: The root of binary tree.
    @return: An integer
    """
    def __init__(self):
        # a mimimum negative value
        self.max_sum = float('-inf')
    
    def maxPathSum(self, root):
        # write your code here
        if root is None:
            return 0
        self.get_max_path_sum(root)
        return self.max_sum
    
    def get_max_path_sum(self, node):
        if node is None:
            return 0
        max_left = self.get_max_path_sum(node.left)
        max_right = self.get_max_path_sum(node.right)
        self.max_sum = max(self.max_sum, max_left + max_right + node.val)
        current_max = node.val + max(max_left, max_right)
        
        return current_max if current_max > 0 else 0

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

