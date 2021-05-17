# Binary Tree Postorder Traversal 68 \(E\)

## Problem

Given a binary tree, return the postorder traversal of its nodes’ values.

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
[2,1,3]
```

Explanation:

   1  
  /  \  
2     3  
It will be serialized as {1,2,3} postorder traversal

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
It will be serialized as {1,\#,2,3} postorder traversalChallenge

Can you do it without recursion?

## Solution - Recursion

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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if not root:
            return 
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - Non-Recursion

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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        stack = []
        prev, curr = None, root

        if not root:
            return result

        stack.append(root)
        while len(stack) > 0:
            curr = stack[-1]
            if not prev or prev.left == curr or prev.right == curr:  # traverse down the tree
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif curr.left == prev:  # traverse up the tree from the left
                if curr.right:
                    stack.append(curr.right)
            else:  # traverse up the tree from the right
                result.append(curr.val)
                stack.pop()
            prev = curr

        return result
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**



