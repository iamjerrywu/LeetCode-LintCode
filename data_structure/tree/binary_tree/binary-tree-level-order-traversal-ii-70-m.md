# Binary Tree Level Order Traversal II 70 \(M\)

## Problem

Given a binary tree, return the bottom-up level order traversal of its nodes' values. \(ie, from left to right, level by level from leaf to root\).Example

**Example 1:**

Input:

```text
tree = {1,2,3}
```

Output:

```text
[[2,3],[1]]
```

Explanation:

```text
    1
   / \
  2   3
```

it will be serialized {1,2,3}  
**Example 2:**

Input:

```text
tree = {3,9,20,#,#,15,7}
```

Output:

```text
[[15,7],[9,20],[3]]
```

Explanation:

```text
    3
   / \
  9  20
    /  \
   15   7
```

it will be serialized {3,9,20,\#,\#,15,7}

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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code her
        res = []
        if not root:
            return res
        
        tmp = []
        tmp.append(root)
        
        while tmp:
            new_tmp = []
            res.append([n.val for n in tmp])
            for node in tmp:
                if node.left:
                    new_tmp.append(node.left)
                if node.right:
                    new_tmp.append(node.right)
            tmp = new_tmp
        res.reverse()
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

