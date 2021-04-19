# Serialize and Deserialize BST 1235 \(M\)

## Problem

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a **binary search tree**. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

**The encoded string should be as compact as possible.**

**Note:** Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.Example

**Example 1:**

```text
Input：[2,1,3]
Output：[2,1,3]
Explanation：
     2
    / \
   1   3
```

**Example 2:**

```text
Input：[1,#,2]
Output：[1,#,2]
Explanation：
  1
   \
    2
```

## Solution - BFS

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
    def serialize(self, root):
        res = []
        if not root:
            return ['#']
        queue = [root]
        while queue:
            node = queue[0]
            if not node:
                res.append('#')
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            queue.pop(0)
        return res

        

    def deserialize(self, data):
        if data[0] == '#':
            return None
        root = TreeNode(int(data.pop(0)))
        queue = [root]
        is_left = True
        while data:
            str = data.pop(0)
            if str != '#':
                node = TreeNode(int(str))
                queue.append(node)
                if is_left:
                    queue[0].left = node
                else:
                    queue[0].right = node
            if not is_left:
                queue.pop(0)
            is_left = not is_left
        return root

        
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

