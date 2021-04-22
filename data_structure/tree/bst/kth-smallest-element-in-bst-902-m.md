# Kth Smallest Element in BST 902 \(M\)

## Problem

Given a binary search tree, write a function `kthSmallest` to find the kth smallest element in it.

You may assume k is always valid, `1 ≤ k ≤ BST's total elements`.Example

**Example 1:**

```text
Input：{1,#,2},2
Output：2
Explanation：
	1
	 \
	  2
The second smallest element is 2.
```

**Example 2:**

```text
Input：{2,1,3},1
Output：1
Explanation：
  2
 / \
1   3
The first smallest element is 1.
```

Challenge

What if the BST is modified \(insert/delete operations\) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

## Solution

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
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        stack = []

        while root:
            stack.append(root)
            root = root.left

        for i in range(k - 1):
            node = stack[-1]

            if not node.right:
                node = stack.pop(-1)
                while len(stack) != 0 and stack[-1].right == node:
                    node = stack.pop(-1) 
            else:
                node = node.right
                while node != None:
                    stack.append(node)
                    node = node.left
        return stack[-1].val         
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

