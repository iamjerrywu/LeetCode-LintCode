# Minimum Subtree 596 \(M\)

## Problem

Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.  
The range of input and output data is in int.

LintCode will print the subtree which root is your return node.  
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.Example

Example 1:

```text
Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5 
The sum of whole tree is minimum, so return the root.
```

Example 2:

```text
Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
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
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        _, min_node, _ = self.helper(root)
        return min_node
    
    def helper(self, root):
        if not root:
            return float('inf'), None, 0
        
        left_min_weight, left_min_node, left_sum = self.helper(root.left)
        right_min_weight, right_min_node, right_sum = self.helper(root.right)
        cur_sum = left_sum + right_sum + root.val
        
        if left_min_weight == min(left_min_weight, right_min_weight, cur_sum):
            return left_min_weight, left_min_node, cur_sum
        if right_min_weight == min(left_min_weight, right_min_weight, cur_sum):
            return right_min_weight, right_min_node, cur_sum
        return cur_sum, root, cur_sum
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

