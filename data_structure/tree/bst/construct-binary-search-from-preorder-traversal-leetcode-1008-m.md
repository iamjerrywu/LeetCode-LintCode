# Construct Binary Search from Preorder Traversal (LeetCode 1008) (M)

## Problem

****

Given an array of integers preorder, which represents the **preorder traversal** of a BST (i.e., **binary search tree**), construct the tree and return _its root_.

It is **guaranteed** that there is always possible to find a binary search tree with the given requirements for the given test cases.

A **binary search tree** is a binary tree where for every node, any descendant of `Node.left` has a value **strictly less than** `Node.val`, and any descendant of `Node.right` has a value **strictly greater than** `Node.val`.

A **preorder traversal** of a binary tree displays the value of the node first, then traverses `Node.left`, then traverses `Node.right`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/03/06/1266.png)

```
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
```

**Example 2:**

```
Input: preorder = [1,3]
Output: [1,null,3]
```

&#x20;

**Constraints:**

* `1 <= preorder.length <= 100`
* `1 <= preorder[i] <= 1000`
* All the values of `preorder` are **unique**.



## Solution - High, Low Bound Recursion

{% tabs %}
{% tab title="Python" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.index = 0
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        return self.dfs(float('-inf'), float('inf'), preorder)
    
    
    def dfs(self, low, high, preorder):
        if self.index == len(preorder):
            return None
        
        cur_val = preorder[self.index]
        
        if cur_val < low or cur_val > high:
            return None
        
        node = TreeNode(cur_val)
        self.index+=1
        node.left = self.dfs(low, cur_val, preorder)
        node.right = self.dfs(cur_val, high, preorder)
        
        return node
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****
