# Binary Tree Right Side View 760 \(M\)

## Problem

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottomExample

**Example 1**

```text
Input: {1,2,3,#,5,#,4}
Output: [1,3,4]
Explanation:
   1            
 /   \
2     3         
 \     \
  5     4       
```

**Example 2**

```text
Input: {1,2,3}
Output: [1,3]
Explanation:
   1            
 /   \
2     3        
```

Tags

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
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    # def __init__(self):
    #     self.res = []
    
    def rightSideView(self, root):
        # write your code here
        view = []
        self.collect(root, 0, view)
        return view
    
    def collect(self, node, depth, view):
        if node:
            if depth == len(view):
                view.append(node.val)
            self.collect(node.right, depth + 1, view)
            self.collect(node.left, depth + 1, view)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

