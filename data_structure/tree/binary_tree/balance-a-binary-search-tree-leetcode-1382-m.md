# Balance a Binary Search Tree (LeetCode 1382) (M)

## Problem



Given the `root` of a binary search tree, return _a **balanced** binary search tree with the same node values_. If there is more than one answer, return **any of them**.

A binary search tree is **balanced** if the depth of the two subtrees of every node never differs by more than `1`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/08/10/balance1-tree.jpg)

```
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/08/10/balanced2-tree.jpg)

```
Input: root = [2,1,3]
Output: [2,1,3]
```

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `1 <= Node.val <= 105`



## Solution&#x20;

First record nodes value in inorder traversal, thus the result is sorted. Then, just transfer a sorted list into Binary Tree

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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        # inorder traversal
        rec = []
        self.dfs(root, rec)
        
        return self.list_to_BST(0, len(rec) - 1, rec)
    
    
    def dfs(self, root, rec):
        if not root:
            return 
        self.dfs(root.left, rec)
        rec.append(root.val)
        self.dfs(root.right, rec)
    
    def list_to_BST(self, start, end, arr):
        if start > end:
            return None
        
        mid = start + (end - start)//2
        
        node = TreeNode(arr[mid])
        node.left = self.list_to_BST(start, mid - 1, arr)
        node.right = self.list_to_BST(mid + 1, end, arr)
        return node)
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

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

