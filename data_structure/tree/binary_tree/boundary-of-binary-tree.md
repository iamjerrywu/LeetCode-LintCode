# Boundary of Binary Tree

## Problem

****

The **boundary** of a binary tree is the concatenation of the **root**, the **left boundary**, the **leaves** ordered from left-to-right, and the **reverse order** of the **right boundary**.

The **left boundary** is the set of nodes defined by the following:

* The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is **empty**.
* If a node in the left boundary and has a left child, then the left child is in the left boundary.
* If a node is in the left boundary, has **no** left child, but has a right child, then the right child is in the left boundary.
* The leftmost leaf is **not** in the left boundary.

The **right boundary** is similar to the **left boundary**, except it is the right side of the root's right subtree. Again, the leaf is **not** part of the **right boundary**, and the **right boundary** is empty if the root does not have a right child.

The **leaves** are nodes that do not have any children. For this problem, the root is **not** a leaf.

Given the `root` of a binary tree, return _the values of its **boundary**_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/11/boundary1.jpg)

<pre><code>Input: root = [1,null,2,3,4]
<strong>Output:
</strong> [1,3,4,2]
Explanation:
- The left boundary is empty because the root does not have a left child.
- The right boundary follows the path starting from the root's right child 2 -> 4.
  4 is a leaf, so the right boundary is [2].
- The leaves from left to right are [3,4].
Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/11/boundary2.jpg)

<pre><code>Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
<strong>Output:
</strong> [1,2,4,7,8,9,10,6,3]
Explanation:
- The left boundary follows the path starting from the root's left child 2 -> 4.
  4 is a leaf, so the left boundary is [2].
- The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
  10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
- The leaves from left to right are [4,7,8,9,10].
Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].</code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `-1000 <= Node.val <= 1000`



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
from collections import deque
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left_bounds = self.find_left_bounds(root.left)
        right_bounds = self.find_right_bounds(root.right)
        footers = self.find_footers(root)
        print(root.val, left_bounds, footers, right_bounds)
        return [root.val] + left_bounds + footers + right_bounds

    def find_left_bounds(self, node):
        if not node:
            return []
        ans = []
        stack = [node]
        while stack:
            node = stack.pop()
            if node.left or node.right:
                ans.append(node.val)
            if node.left:
                stack.append(node.left)
            elif node.right:
                stack.append(node.right)
        
        return ans
    
    def find_right_bounds(self, node):
        if not node:
            return []
        ans = []
        stack = [node]
        while stack:
            node = stack.pop()
            if node.left or node.right:
                ans.append(node.val)
            if node.right:
                stack.append(node.right)
            elif node.left:
                stack.append(node.left)
        
        return ans[::-1]
    
    # def find_footers(self, node):
    #     if not node or (not node.left and not node.right):
    #         return []
    #     ans = []
    #     stack = [node]
    #     # using iterative way to do pre-order traverse using stack
    #     while stack:
    #         node = stack.pop()
    #         # print(node.val)
    #         if not node.left and not node.right:
    #             ans.append(node.val)
    #         # if node.left:
    #         #     stack.append(node.left)
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)
    #     return ans
    
    # recursive way to to pre-order traversal
    def find_footers(self, node):
        if not node or (not node.left and not node.right):
            return []
        
        ans = []
        self.dfs(node, ans)
        return ans
    
    def dfs(self, node, ans):
        if not node.left and not node.right:
            ans.append(node.val)
        if node.left:
            self.dfs(node.left, ans)
        if node.right:
            self.dfs(node.right, ans)
        
        
        
    
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
