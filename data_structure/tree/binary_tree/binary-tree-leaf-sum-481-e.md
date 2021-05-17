# Binary Tree Leaf Sum 481 \(E\)

## Problem

Description

Given a binary tree, calculate the sum of leaves.Example

**Example 1:**

```text
Input：{1,2,3,4}
Output：7
Explanation：
    1
   / \
  2   3
 /
4
3+4=7
```

**Example 2:**

```text
Input：{1,#,3}
Output：3
Explanation：
    1
      \
       3
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
    @param root: the root of the binary tree
    @return: An integer
    """
    def leafSum(self, root):
        # write your code here
        self.res = 0
        self.dfs(root)
        return self.res
        
    def dfs(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.res+=root.val
        self.dfs(root.left)
        self.dfs(root.right)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

