# Flatten Binary Tree to Linked List 453 \(E\)

## Problem

Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the _right_ pointer in TreeNode as the _next_ pointer in ListNode.

Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.Example

**Example 1:**

```text
Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
```

**Example 2:**

```text
Input:{1}
Output:{1}
Explanation：
         1
         1
```

Challenge

Do it in-place without any extra memory.

## Solution - Divide Conquer \(Wrong Example using Global variable\)

### Code

{% hint style="danger" %}
Following case would lead to error, since using global variable, might change the root.right value
{% endhint %}

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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    prev_node = None
    def flatten(self, root):
        # write your code here
        if not root:
            return 
        
        if self.prev_node:
            self.prev_node.left = None
            self.prev_node.right = root
        
        self.prev_node = root
        self.flatten(root.left)
        # here the root.right might be modified due to global variable: self.prev_node.right
        self.flatten(root.right)

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

