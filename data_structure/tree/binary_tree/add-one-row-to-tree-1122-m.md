# Add One Row to Tree 1122 \(M\)

## Problem

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

The given d is in range \[1, maximum depth of the given tree + 1\].  
The given binary tree has at least one tree node.Example

**Example1**

```text
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   
v = 1
d = 2
Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   
```

**Example2**

```text
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   
v = 2
d = 1
Output: 
         2
  	/
       4
     /   \
    2     6
   / \   / 
  3   1 5     
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
    @param v: a integer
    @param d: a integer
    @return: return a TreeNode
    """
    def addOneRow(self, root, v, d):
        # write your code here
        return self.dfs(root, v, d, True)
    
    def dfs(self, root, v, d, is_left):
        if d == 1:
            node = TreeNode(v)
            if is_left:
                node.left = root
            else:
                node.right = root
            return node
        if not root:
            return
        root.left = self.dfs(root.left, v, d - 1, True)
        root.right = self.dfs(root.right, v, d- 1, False)
        return root
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

