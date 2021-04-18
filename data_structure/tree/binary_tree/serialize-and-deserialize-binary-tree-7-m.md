# Serialize and Deserialize Binary Tree 7 \(M\)

## Problem

Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

There is no limit on how to serialize or deserialize a binary tree，you just need to ensure the binary tree can be serialized to a string，and the string can be deserialized to original binary tree.

There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of `serialize` as the input of `deserialize`, it won't check the result of serialize.Example

**Example 1:**

Input:

```text
tree = {3,9,20,#,#,15,7}
```

Output:

```text
{3,9,20,#,#,15,7}
```

Explanation:

Binary tree {3,9,20,\#,\#,15,7}, denote the following structure:  
　　　3  
　　/　＼  
　　9　20  
　　　/　＼  
　　　15　　7  
it will be serialized {3,9,20,\#,\#,15,7}

**Example 2:**

Input:

```text
tree = {1,2,3}
```

Output:

```text
{1,2,3}
```

Explanation:

Binary tree {1,2,3}, denote the following structure:  
　　1  
　/　＼  
　2　3  
it will be serialized {1,2,3}  


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

# from collections import deque
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return ['#']
        queue = [root]
        res = []
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
                

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
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

