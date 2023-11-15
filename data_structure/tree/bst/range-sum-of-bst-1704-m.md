# Range Sum of BST 1704 (M)

## Problem

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

The number of nodes in the tree is at most 10000.\
The final answer is guaranteed to be less than 2^31.Example

**Example 1:**

```
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
```

**Example 2:**

```
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
```

## Solution - Divide Conquer

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
    @param root: the root node
    @param L: an integer
    @param R: an integer
    @return: the sum
    """
    def rangeSumBST(self, root, L, R):
        # write your code here.
        if not root:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
  * n: total amounts of nodes
* **Space Complexity: O(h)**
  * h: height of the tree (can be worst as n), call stack frame



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
    @param root: the root node
    @param L: an integer
    @param R: an integer
    @return: the sum
    """
    def rangeSumBST(self, root, L, R):
        # write your code here.
        cnt = [0]
        self.dfs(root, L, R, cnt)
        return cnt[0]
    
    def dfs(self, root, L, R, cnt):
        if not root:
            return 0
        self.dfs(root.left, L, R, cnt)
        if L <= root.val <= R:
            cnt[0]+=root.val
        self.dfs(root.right, L, R, cnt)
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(h)**
  * h is the BST height
* **Space Complexity: O(h)**
  * h: height of the tree,&#x20;
