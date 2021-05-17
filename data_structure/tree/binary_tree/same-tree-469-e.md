# Same Tree 469 \(E\)

## Problem



Description

Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.Example

**Example 1:**

```text
Input:{1,2,2,4},{1,2,2,4}
Output:true
Explanation:
        1                   1
       / \                 / \
      2   2   and         2   2
     /                   /
    4                   4

are identical.
```

**Example 2:**

```text
Input:{1,2,3,4},{1,2,3,#,4}
Output:false
Explanation:

        1                  1
       / \                / \
      2   3   and        2   3
     /                        \
    4                          4

are not identical.
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
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # write your code here
        
        if not a and not b:
            return True
        elif not a or not b:
            return False
        elif a.val != b.val:
            return False
        
        return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

