# Binary Tree Zigzag Level Order Traversal 71 \(M\)

## Problem

Given a binary tree, return the zigzag level order traversal of its nodes' values. \(ie, from left to right, then right to left for the next level and alternate between\).Example

**Example 1:**

Input:

```text
tree = {1,2,3}
```

Output:

```text
[[1],[3,2]]
```

Explanation:

```text
    1
   / \
  2   3
```

it will be serialized {1,2,3}  
**Example 2:**

Input:

```text
tree = {3,9,20,#,#,15,7}
```

Output:

```text
[[3],[20,9],[15,7]]
```

Explanation:

```text
    3
   / \
  9  20
    /  \
   15   7
```

it will be serialized {3,9,20,\#,\#,15,7}

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
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        lists = []
        if not root:
            return lists
        
        q = collections.deque()
        is_left_to_right = True
        #put from right
        q.append(root)
        
        while len(q) != 0:
            size = len(q)
            l = []
            for i in range(size):
                node = q.popleft()
                l.append(node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if not is_left_to_right:
                l.reverse()
            
            lists.append(l)
            is_left_to_right = not is_left_to_right
        
        return lists
            

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

