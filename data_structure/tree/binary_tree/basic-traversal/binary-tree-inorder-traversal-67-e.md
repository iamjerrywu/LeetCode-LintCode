# Binary Tree Inorder Traversal 67 \(E\)

## Problem

Given a binary tree, return the inorder traversal of its nodes‘ values.Example

**Example 1:**

Input:

```text
binary tree = {1,2,3}
```

Output:

```text
[2,1,3]
```

Explanation:

   1  
  /  \  
2     3  
It will be serialized as {1,2,3} inorder traversal

**Example 2:**

Input:

```text
binary tree = {1,#,2,3}
```

Output:

```text
[1,3,2]
```

Explanation:

1  
  \  
   2  
  /  
3  
It will be serialized as {1,\#,2,3} inorder traversalChallenge

Can you do it without recursion?

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
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return self.res
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
        return self.res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

