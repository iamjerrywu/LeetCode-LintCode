# Lowest Common Ancestor III 578 (M)

## Problem

Description

Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.\
The nearest common ancestor of two nodes refers to the nearest common node among all the parent nodes of two nodes (including the two nodes).\
Return `null` if LCA does not exist.

**node A or node B may not exist in tree.**\
Each node has a different valueExample

**Example1**

```
Input: 
{4, 3, 7, #, #, 5, 6}
3 5
5 6
6 7 
5 8
Output: 
4
7
7
null
Explanation:
  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
LCA(5, 8) = null

```

**Example2**

```
Input:
{1}
1 1
Output: 
1
Explanation:
The tree is just a node, whose value is 1.
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
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        A_exist, B_exist, node = self.helper(root, A, B)
        if A_exist and B_exist:
            return node
        return None
        
    def helper(self, node, A, B):
        if not node:
            return False, False, None
        A_exist_left, B_exist_left, left = self.helper(node.left, A, B)
        A_exist_right, B_exist_right, right = self.helper(node.right, A, B)
        
        A_exist = A_exist_left | A_exist_right | (node == A)
        B_exist = B_exist_left | B_exist_right | (node == B)
        
        if node == A or node == B:
            return A_exist, B_exist, node
        if left and right:
            return A_exist, B_exist, node
        if left:
            return A_exist, B_exist, left
        if right:
            return A_exist, B_exist, right
        return A_exist, B_exist, None
```
{% endtab %}

{% tab title="Python (Better)" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node, cnt = self.dfs(root, p, q)
        if cnt < 2:
            return None
        return node
    
    def dfs(self, node, p, q):
        if not node:
            return None, 0
        
        left, l_cnt = self.dfs(node.left, p, q)
        right, r_cnt = self.dfs(node.right, p, q)
        cnt = l_cnt + r_cnt
        if node == p or node == q:
            return node, cnt + 1
        if left and right:
            return node, 2
        
        if left:
            return left, cnt
        return right, cnt
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
