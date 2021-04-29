# Equal Tree Partition 864 \(M\)

## Problem

Description

Given a binary tree with `n` nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing **exactly** one edge on the original tree.

1. The range of tree node value is in the range of `[-100000, 100000]`.
2. `1 <= n <= 10000`
3. You can assume that the tree is not `null` [Binary Tree Representation](https://www.lintcode.com/help/binary-tree-representation/)

Example

**Example 1:**

```text
Input: {5,10,10,#,#,2,3}
Output: true
Explanation:
  origin:
     5
    / \
   10 10
     /  \
    2    3
  two subtrees:
     5       10
    /       /  \
   10      2    3
```

**Example 2:**

```text
Input: {1,2,10,#,#,2,20}
Output: false
Explanation:
  origin:
     1
    / \
   2  10
     /  \
    2    20
```

## Solution - DFS

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
    @param root: a TreeNode
    @return: return a boolean
    """
    def checkEqualTree(self, root):
        # write your code here
        self.mp = {}
        sum = self.dfs(root)
        if sum == 0:
            # should be at least twice, since whole tree is 0 and one subtree is 0 
            return self.mp[0] > 1
        # should write get(sum//2), otherwise may got key error
        return sum%2 == 0 and self.mp.get(sum//2) != None
    def dfs(self, root):
        if not root:
            return 0
        sum = root.val + self.dfs(root.left) + self.dfs(root.right)
        self.mp[sum] = self.mp.get(sum, 0) + 1
        return sum

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

