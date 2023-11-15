# Sum of Root To Leaf Binary Numbers (LeetCode 1022) (E)

## Problem



You are given the `root` of a binary tree where each node has a value `0` or `1`. Each root-to-leaf path represents a binary number starting with the most significant bit.

* For example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent `01101` in binary, which is `13`.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return _the sum of these numbers_.

The test cases are generated so that the answer fits in a **32-bits** integer.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png)

```
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```

**Example 2:**

```
Input: root = [0]
Output: 0
```

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 1000]`.
* `Node.val` is `0` or `1`.



## Solution&#x20;

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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    
     
    def dfs(self, node, path_val):
        ans = 0
        if not node:
            return 0
        path_val = path_val * 2 + node.val
        
        if not node.left and not node.right:
            ans+=path_val
        ans+=self.dfs(node.left, path_val)
        ans+=self.dfs(node.right, path_val)
        return ans
        
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

