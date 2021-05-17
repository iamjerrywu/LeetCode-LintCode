# Tweaked Identical Binary Tree 470 \(E\)

## Problem

Check whether two binary trees are equivalent after several twists. Twist is defined as exchanging left and right subtrees of any node. The definition of equivalence is that two binary trees must have the same structure, and the values of nodes in corresponding positions must be equal.

There is no two nodes with the same value in the tree.Example

**Example 1:**

```text
Input:{1,2,3,4},{1,3,2,#,#,#,4}
Output:true
Explanation:
        1             1
       / \           / \
      2   3   and   3   2
     /                   \
    4                     4

are identical.
```

**Example 2:**

```text
Input:{1,2,3,4},{1,3,2,4} 
Output:false
Explanation:

        1             1
       / \           / \
      2   3   and   3   2
     /             /
    4             4

are not identical.
```

Challenge

O\(n\) time

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
    @return: true if they are tweaked identical, or false.
    """
    def isTweakedIdentical(self, a, b):
        # write your code here
        if a == None and b == None:
            return True
        if a and b and a.val == b.val:
            return self.isTweakedIdentical(a.left, b.left) and self.isTweakedIdentical(a.right, b.right) or \
                        self.isTweakedIdentical(a.left, b.right) and self.isTweakedIdentical(a.right, b.left)
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

