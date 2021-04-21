# Subtree with Maximum Average 597 \(M\)

## Problem

Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

LintCode will print the subtree which root is your return node.  
It's guaranteed that there is only one subtree with maximum average.Have you met this question in a real interview?  YesProblem Correction

#### Example

**Example 1**

```text
Input：
{1,-5,11,1,2,4,-2}
Output：11
Explanation:
The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
The average of subtree of 11 is 4.3333, is the maximun.
```

**Example 2**

```text
Input：
{1,-5,11}
Output：11
Explanation:
     1
   /   \
 -5     11
The average of subtree of 1,-5,11 is 2.333,-5,11. So the subtree of 11 is the maximun.
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
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    node, average = None, 0
    def findSubtree2(self, root):
        # write your code here
        if not root:
            return
        self.helper(root)
        return self.node

    def helper(self, node): 
        if not node:
            return 0, 0
        left_sum, left_size = self.helper(node.left)
        right_sum, right_size = self.helper(node.right)
        
        node_sum = left_sum + right_sum + node.val
        size = left_size + right_size + 1
        
        if self.node is None or node_sum / size > self.average:
            self.node = node
            self.average = node_sum / size
        return node_sum, size
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

