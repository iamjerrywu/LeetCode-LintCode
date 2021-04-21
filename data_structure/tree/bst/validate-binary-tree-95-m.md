# Validate Binary Search Tree 95 \(M\)

## Problem



Given a binary tree, determine if it is a valid binary search tree \(BST\).

Assume a BST is defined as follows:

* The left subtree of a node contains only nodes with keys **less than** the node's key.
* The right subtree of a node contains only nodes with keys **greater than** the node's key.
* Both the left and right subtrees must also be binary search trees.
* A single node tree is a BST

Example

**Example 1:**

```text
Input:  {-1}
Output：true
Explanation：
For the following binary tree（only one node）:
	      -1
This is a binary search tree.
```

**Example 2:**

```text
Input:  {2,1,4,#,#,3,5}
Output: true
For the following binary tree:
	  2
	 / \
	1   4
	   / \
	  3   5
This is a binary search tree.
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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def __init__(self):
        self.res = []
    
    def isValidBST(self, root):
        # write your code here
        self.inorder_traverse(root)
        for i in range(1, len(self.res)):
            if self.res[i]<= self.res[i - 1]:
                return False
        return True
    
    def inorder_traverse(self, root):
        if not root:
            return 
        self.inorder_traverse(root.left)
        self.res.append(root.val)
        self.inorder_traverse(root.right)
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

