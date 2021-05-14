# Binary Tree Vertical Order Traversal 651 \(M\)

## Problem

Given a binary tree, return the vertical order traversal of its nodes' values. \(ie, from top to bottom, column by column\).

If two nodes are in the same row and column, the order should be from **left to right**.Example

**Example1**

```text
Inpurt:  {3,9,20,#,#,15,7}
Output: [[9],[3,15],[20],[7]]
Explanation:
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
```

**Example2**

```text
Input: {3,9,8,4,0,1,7}
Output: [[4],[9],[3,0,1],[8],[7]]
Explanation:
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
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
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        records = collections.defaultdict(list)
        queue = collections.deque()

        queue.append((root, 0))
        while queue:
            node, col_idx = queue.popleft()
            if node:
                records[col_idx].append(node.val)
                queue.append((node.left, col_idx - 1))
                queue.append((node.right, col_idx + 1))
        return [records[i] for i in sorted(records)]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogn\)**
  * Tree traversal: O\(n\)
  * Sort: O\(nlogn\)
* **Space Complexity: O\(n\)**

