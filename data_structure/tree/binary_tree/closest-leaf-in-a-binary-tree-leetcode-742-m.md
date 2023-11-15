# Closest Leaf in a Binary Tree (LeetCode 742) (M)

## Problem

Given the `root` of a binary tree where every node has **a unique value** and a target integer `k`, return _the value of the **nearest leaf node** to the target_ `k` _in the tree_.

**Nearest to a leaf** means the least number of edges traveled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/06/13/closest1-tree.jpg)

```
Input: root = [1,3,2], k = 1
Output: 2
Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/06/13/closest2-tree.jpg)

```
Input: root = [1], k = 1
Output: 1
Explanation: The nearest leaf node is the root node itself.
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2021/06/13/closest3-tree.jpg)

```
Input: root = [1,2,3,4,null,null,null,5,null,6], k = 2
Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
```

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 1000]`.
* `1 <= Node.val <= 1000`
* All the values of the tree are **unique**.
* There exist some node in the tree where `Node.val == k`.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    
    def __init__(self):
        self.tar_node = None
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph = collections.defaultdict(list)
        is_leaf = {}
        parent = None
        self.dfs(root, parent, graph, is_leaf, k)
        queue = collections.deque([self.tar_node])
        visited = {self.tar_node}
        return self.bfs(queue, graph, k, is_leaf, visited)

    def dfs(self, node, parent, graph, is_leaf, k):
        if not node:
            return 
        if node.val ==  k:
            self.tar_node = node
        if parent:
            graph[node].append(parent)
            graph[parent].append(node)
        
        if not node.left and not node.right:
            is_leaf[node] = True
        else:
            is_leaf[node] = False
        
        self.dfs(node.left, node, graph, is_leaf, k)
        self.dfs(node.right, node, graph, is_leaf, k)
    
    def bfs(self, queue, graph, k, is_leaf, visited):
        ans = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if is_leaf[cur]:
                    return cur.val

                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

