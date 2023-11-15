# Find Largest Value in Each Tree Row (LeetCode 515) (M)

## Problem



Given the `root` of a binary tree, return _an array of the largest value in each row_ of the tree **(0-indexed)**.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/21/largest\_e1.jpg)

```
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
```

**Example 2:**

```
Input: root = [1,2,3]
Output: [1,3]
```

&#x20;

**Constraints:**

* The number of nodes in the tree will be in the range `[0, 104]`.
* `-231 <= Node.val <= 231 - 1`



## Solution - BFS

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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        queue = collections.deque([root])
        
        ans = []
        while queue:
            max_val = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(max_val)
        return ans
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



## Solution - DFS

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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        rec = {}
        self.dfs(root, 0, rec)
        return [val for k, val in rec.items()]
        
    
    def dfs(self, node, level, rec):
        if not node:
            return 0
        
        if level in rec:
            rec[level] = max(rec[level], node.val)
        else:
            rec[level] = node.val
        
        self.dfs(node.left, level + 1, rec)
        self.dfs(node.right, level + 1, rec)
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

