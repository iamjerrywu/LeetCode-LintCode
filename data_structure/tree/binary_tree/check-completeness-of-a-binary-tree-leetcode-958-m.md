# Check Completeness of a Binary Tree (LeetCode 958) (M)

## Problem

Given the `root` of a binary tree, determine if it is a _complete binary tree_.

In a [**complete binary tree**](http://en.wikipedia.org/wiki/Binary\_tree#Types\_of\_binary\_trees), every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between `1` and `2h` nodes inclusive at the last level `h`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png)

```
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png)

```
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
```

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 100]`.
* `1 <= Node.val <= 1000`

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
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([(0, root)])
        
        prev = -1
        while queue:
            for _ in range(len(queue)):
                idx, node = queue.popleft()
                if idx != prev + 1:
                    return False
                
                if node.left:
                    queue.append((idx * 2 + 1, node.left))
                if node.right:
                    queue.append((idx * 2 + 2,  node.right))
                prev+=1
        return True
                
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

* **Time Complexity:**&#x20;
* **Space Complexity:**

