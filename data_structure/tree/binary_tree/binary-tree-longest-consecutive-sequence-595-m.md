# Binary Tree Longest Consecutive Sequence 595 (M)

## Problem

Given the `root` of a binary tree, return _the length of the longest consecutive sequence path_.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).

**Example 1:**![](https://assets.leetcode.com/uploads/2021/03/14/consec1-1-tree.jpg)

```
Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/03/14/consec1-2-tree.jpg)

```
Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
```

**Constraints:**

* The number of nodes in the tree is in the range `[1, 3 * 104]`.
* `-3 * 104 <= Node.val <= 3 * 104`

## Solution

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
        self.max_length = 1
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.dfs(root, self.max_length, 1, float('inf'))
        return self.max_length
    
    def dfs(self, node, max_length, length, parent_val):
        if not node:
            return 
        
        if node.val == parent_val+1:
            length+=1
        else:
            length = 1
        self.max_length = max(self.max_length, length)
        parent_val = node.val
        self.dfs(node.left, self.max_length, length, parent_val)
        self.dfs(node.right, self.max_length, length, parent_val)
        
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**

## Solution

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
    # def __init__(self):
    #     self.max_length = 1
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = self.dfs(root, 1, float('inf'))
        return ans
    
    def dfs(self, node, length, parent_val):
        if not node:
            return length 
        
        if node.val == parent_val+1:
            length+=1
        else:
            length = 1
        parent_val = node.val
        left_max = self.dfs(node.left, length, parent_val)
        right_max = self.dfs(node.right, length, parent_val)
        return max(left_max, right_max, length)
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
