# Binary Tree Right Side View 760 (M)

## Problem

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottomExample

**Example 1**

```
Input: {1,2,3,#,5,#,4}
Output: [1,3,4]
Explanation:
   1            
 /   \
2     3         
 \     \
  5     4       
```

**Example 2**

```
Input: {1,2,3}
Output: [1,3]
Explanation:
   1            
 /   \
2     3        
```

Tags

## Solution - DFS

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
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    # def __init__(self):
    #     self.res = []
    
    def rightSideView(self, root):
        # write your code here
        view = []
        self.collect(root, 0, view)
        return view
    
    def collect(self, node, depth, view):
        if node:
            if depth == len(view):
                view.append(node.val)
            self.collect(node.right, depth + 1, view)
            self.collect(node.left, depth + 1, view)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - BFS

###

### Code

{% tabs %}
{% tab title="python" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        queue = collections.deque([(root, 0)])
        
        res = []
        cur_level = 0
        while queue:
            for _ in range(len(queue)):
                cur, level = queue.popleft()
                if level == cur_level:
                    res.append(cur.val)
                    cur_level+=1
                if cur.right:
                    queue.append((cur.right, cur_level))
                if cur.left:
                    queue.append((cur.left, cur_level))
        return res
            
        
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
