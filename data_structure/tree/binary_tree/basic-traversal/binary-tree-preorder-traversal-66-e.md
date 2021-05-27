# Binary Tree Preorder Traversal 66 \(E\)

## Problem

Description

Given a binary tree, return the preorder traversal of its nodes' values.

* The first data is the root node, followed by the value of the left and right son nodes, and "\#" indicates that there is no child node.
* The number of nodes does not exceed 20.

Example

**Example 1:**

Input:

```text
binary tree = {1,2,3}
```

Output:

```text
[1,2,3]
```

Explanation:

   1  
  /  \  
2     3  
It will be serialized as {1,2,3} preorder traversal

**Example 2:**

Input:

```text
binary tree = {1,#,2,3}
```

Output:

```text
[1,2,3]
```

Explanation:

1  
  \  
   2  
  /  
3  
It will be serialized as {1,\#,2,3} preorder traversalChallenge

Can you do it without recursion?

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
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        res = []
        self.helper(root, res)
        return res
    def helper(self,node, res):
        if not node:
            return
        res.append(node.val)
        self.helper(node.left, res)
        self.helper(node.right, res)


```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - Iteration using Stack

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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        stack = [root]
        preorder = []

        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

