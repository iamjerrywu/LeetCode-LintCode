# Convert Sorted Array to Binary Search Tree With Minimal Height 177 \(E\)

## Problem

Given a sorted \(increasing order\) array, Convert it to a binary search tree with minimal height.

There may exist multiple valid solutions, return any of them.Example

**Example 1:**

```text
Input: []
Output:  {}
Explanation: The binary search tree is null
```

**Example 2:**

```text
Input: [1,2,3,4,5,6,7]
Output:  {4,2,6,1,3,5,7}
Explanation:
A binary search tree with minimal height.

         4
       /   \
      2     6
     / \    / \
    1   3  5   7
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
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        return self.convert(A, 0, len(A) - 1)
        
    def convert(self, A, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(A[start])
        mid = (start + end) // 2
        root = TreeNode(A[mid])
        root.left = self.convert(A, start, mid - 1)
        root.right = self.convert(A, mid + 1, end)
        return root
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

