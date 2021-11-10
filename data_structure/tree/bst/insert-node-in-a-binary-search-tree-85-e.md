# Insert Node in a Binary Search Tree 85 (E)

## Problem

Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

You can assume there is no duplicate values in this tree + node.Example

**Example 1:**

Input:

```
tree = {}
node= 1
```

Output:

```
{1}
```

Explanation:

Insert node 1 into the empty tree, so there is only one node on the tree.

**Example 2:**

Input:

```
tree = {2,1,4,#,#,3}
node = 6
```

Output:

```
{2,1,4,#,#,3,6}
```

Explanation:

&#x20;    2                              2\
&#x20;  /   \                          /   \\\
&#x20;1     4          -->       1       4\
&#x20;      /                                /  \\\
&#x20;   3                                3      6Challenge

Can you do it without recursion?

## Solution&#x20;

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
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    # def insert_helper(self, root, node):
        
    
    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node
        if root.val > node.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
        return root
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
