# Search in a Binary Search Tree 1524 \(E\)

## Problem

Given the root of a binary search tree \(BST\) and a `value`.

Return the node whose value equals the given `value`. If such node doesn't exist, return `null`.Example

**Example 1:**

```text
Input: value = 2
        4
       / \
      2   7
     / \
    1   3
Output: node 2
```

**Example 2:**

```text
Input: value = 5
        4
       / \
      2   7
     / \
    1   3
Output: null
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
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def searchBST(self, root, val):
        # Write your code here.
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

