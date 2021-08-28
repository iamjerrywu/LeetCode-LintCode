# Diameter of Binary Tree 1181 \(E\)

## Problem

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree.

The length of path between two nodes is represented by the number of edges between them.Example

**Example 1:**

```text
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**

```text
Input:[2,3,#,1]
Output:2

Explanation:
      2
    /
   3
 /
1
```

## Solution - DFS without Global Variables

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
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        
        max_d, max_c = self.dfs(root)
        return max_d
    
    def dfs(self, node):
        if not node:
            return 0, 0
        left_max_d, left_max_c = self.dfs(node.left)
        right_max_d, right_max_c = self.dfs(node.right)

        max_d = max(left_max_d, right_max_d, left_max_c + right_max_c)
        max_c = max(left_max_c, right_max_c) + 1

        return max_d, max_c
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**
  * O\(n\) in worst case as tree like linkedlist
  * O\(logn\) in best case as balanced tree

## Solution - DFS without Global Variables

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
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        
        max_d, max_c = self.dfs(root)
        return max_d
    
    def dfs(self, node):
        if not node:
            return 0, 0
        left_max_d, left_max_c = self.dfs(node.left)
        right_max_d, right_max_c = self.dfs(node.right)

        max_d = max(left_max_d, right_max_d, left_max_c + right_max_c)
        max_c = max(left_max_c, right_max_c) + 1

        return max_d, max_c
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**
  * O\(n\) in worst case as tree like linkedlist
  * O\(logn\) in best case as balanced tree

