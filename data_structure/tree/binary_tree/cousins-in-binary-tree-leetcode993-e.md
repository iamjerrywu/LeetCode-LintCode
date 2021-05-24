# Cousins in Binary Tree \(LeetCode993\) \(E\)

## Problem

In a binary tree, the root node is at depth `0`, and children of each depth `k` node are at depth `k+1`.

Two nodes of a binary tree are _cousins_ if they have the same depth, but have **different parents**.

We are given the `root` of a binary tree with unique values, and the values `x` and `y` of two different nodes in the tree.

Return `true` if and only if the nodes corresponding to the values `x` and `y` are cousins.

**Example 1:**  
![](https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png)

```text
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
```

**Example 2:**  
![](https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png)

```text
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png)

```text
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
```

**Constraints:**

* The number of nodes in the tree will be between `2` and `100`.
* Each node has a unique integer value from `1` to `100`.

## Solution - BFS

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
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        queue = collections.deque([root])
        
        while queue:
            siblings = False
            cousins = False
            nodes_at_depth = len(queue)
            for _ in range(nodes_at_depth):
                
                node = queue.popleft()
                
                if node is None:
                    siblings = False
                else:
                    if node.val == x or node.val == y:
                        if not cousins:
                            siblings, cousins = True, True
                        else:
                            return not siblings 
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                    queue.append(None)
            
            if cousins:
                return False
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

