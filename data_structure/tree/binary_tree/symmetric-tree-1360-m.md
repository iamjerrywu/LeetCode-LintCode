# Symmetric Tree 1360 \(M\)

## Problem

Given a binary tree, check whether it is a mirror of itself \(ie, symmetric around its center\).Example

**Example1**

```text
Input: {1,2,2,3,4,4,3}Output: trueExplanation:    1   / \  2   2 / \ / \3  4 4  3This binary tree {1,2,2,3,4,4,3} is symmetric
```

**Example2**

```text
Input: {1,2,2,#,3,#,3}Output: falseExplanation:    1   / \  2   2   \   \   3    3This is not a symmetric tree
```

Challenge

Could you solve it both recursively and iteratively?

## Solution - Recursion DFS

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
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
        return self._is_symmetric(root.left, root.right)
    
    def _is_symmetric(self, left_root, right_root):
        if not left_root and not right_root:
            return True
        if not left_root or not right_root:
            return False
        if left_root.val != right_root.val:
            return False
        
        # WARNING!
        # the symmetric policy!
        # left_root.left <-> right_root.right
        # left_root.right <-> right_root.left
        left_symmetric = self._is_symmetric(left_root.left, right_root.right)
        right_symmetric = self._is_symmetric(left_root.right, right_root.left)

        return left_symmetric and right_symmetric
        


```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n/2\)**
  * Each pair \(left, right\) node would be traversed, and each node only be traversed once
* **Space Complexity:**

