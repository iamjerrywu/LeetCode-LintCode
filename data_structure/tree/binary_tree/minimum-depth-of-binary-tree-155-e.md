# Minimum Depth of Binary Tree 155 \(E\)

## Problem

Description

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.Example

**Example 1:**

```text
Input: {}
Output: 0
```

**Example 2:**

```text
Input:  {1,#,2,3}
Output: 3	
Explanation:
	1
	 \ 
	  2
	 /
	3    
it will be serialized {1,#,2,3}
```

**Example 3:**

```text
Input:  {1,2,3,#,#,4,5}
Output: 2	
Explanation: 
      1
     / \ 
    2   3
       / \
      4   5  
it will be serialized {1,2,3,#,#,4,5}
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
from collections import deque
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
        queue = deque([root])
        min_depth = 0
        while queue:
            min_depth+=1
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return min_depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)             
        return min_depth

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

