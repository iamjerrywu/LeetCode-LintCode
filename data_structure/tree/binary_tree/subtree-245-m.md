# Subtree 245 \(M\)

## Problem

You have two very large binary trees: `T1`, with millions of nodes, and `T2`, with hundreds of nodes. Create an algorithm to decide if `T2` is a subtree of `T1`.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.Example

**Example 1:**

```text
Input：{1,2,3,#,#,4},{3,4}
Output：true
Explanation：
T2 is a subtree of T1 in the following case:
           1                3
          / \              / 
    T1 = 2   3      T2 =  4
            /
           4
```

**Example 2:**

```text
Input：{1,2,3,#,#,4},{3,#,4}
Output：false
Explanation：
T2 isn't a subtree of T1 in the following case:

           1               3
          / \               \
    T1 = 2   3       T2 =    4
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
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def isSubtree(self, T1, T2):
        # write your code here
        if T2 is None:
            return True
        
        if T1 is None:
            return False
            
        if self.is_equal(T1, T2):
            return True
        
        return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
    
    def is_equal(self, T1, T2):
        if T1 is None and T2 is None: 
            return True
        
        if T1 is None or T2 is None:
            return False
        
        if T1.val != T2.val:
            return False
        
        return self.is_equal(T1.left, T2.left) and self.is_equal(T1.right, T2.right)
            
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

