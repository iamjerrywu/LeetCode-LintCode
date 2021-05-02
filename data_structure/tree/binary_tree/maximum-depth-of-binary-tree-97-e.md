# Maximum Depth of Binary Tree 97 \(E\)

## Problem



Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

The answer will not exceed `5000`Example

**Example 1:**

```text
Input: tree = {}
Output: 0
Explanation: The height of empty tree is 0.
```

**Example 2:**

```text
Input: tree = {1,2,3,#,#,4,5}
Output: 3	
Explanation: Like this:
   1
  / \                
 2   3                
    / \                
   4   5
it will be serialized {1,2,3,#,#,4,5}
```

## Solution - DFS

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
    def maxDepth(self, root):
        # write your code here
        self.res = 0
        self.dfs(root, 1)
        return self.res
        
    def dfs(self, root, cur_h):
        if not root:
            return
        self.res = max(self.res, cur_h)
        self.dfs(root.left, cur_h + 1)
        self.dfs(root.right, cur_h + 1)
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - Divide Conquer

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
    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0
        return self.dc(root)
    def dc(self, node):
        if not node:
            return 0

        left = self.dc(node.left)
        right = self.dc(node.right)
        
        return max(left, right) + 1
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

