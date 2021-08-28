# Template

## Problem

Given the `root` of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in `to_delete`, we are left with a forest \(a disjoint union of trees\).

Return the roots of the trees in the remaining forest. You may return the result in any order.

**Example 1:**![](https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png)

```text
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
```

**Example 2:**

```text
Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
```

**Constraints:**

* The number of nodes in the given tree is at most `1000`.
* Each node has a distinct value between `1` and `1000`.
* `to_delete.length <= 1000`
* `to_delete` contains distinct values between `1` and `1000`

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
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []
        self.dfs(root, to_delete_set, True, res)
        return res
    
    def dfs(self, root, to_delete_set, is_root, res):
        if not root:
            return
        root_deleted = root.val in to_delete_set
        if is_root and not root_deleted:
            res.append(root)
        root.left = self.dfs(root.left, to_delete_set, root_deleted, res)
        root.right = self.dfs(root.right, to_delete_set, root_deleted, res)
        return None if root_deleted else root
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
  * n: total nodes amount
* **Space Complexity: O\(logn\)**
  * Recursion stack

