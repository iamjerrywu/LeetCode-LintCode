# Diameter of N-Ary Tree (LeetCode 1522) (M)

## Problem

Given a `root` of an [N-ary tree](https://leetcode.com/articles/introduction-to-n-ary-trees/), you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the **longest** path between any two nodes in the tree. This path may or may not pass through the root.

(_Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)_

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/07/19/sample\_2\_1897.png)

```
Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Explanation: Diameter is shown in red color.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/07/19/sample\_1\_1897.png)

```
Input: root = [1,null,2,null,3,4,null,5,null,6]
Output: 4
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/07/19/sample\_3\_1897.png)

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 7
```

&#x20;

**Constraints:**

* The depth of the n-ary tree is less than or equal to `1000`.
* The total number of nodes is between `[1, 104]`.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        max_h, max_d = self.dfs(root)
        return max_d
    
    def dfs(self, root):
        
        if not root:
            return 0, 0
        
        all_child_h = []
        all_child_d = []
        
        for child in root.children:
            child_h, child_d = self.dfs(child)
            all_child_h.append(child_h)
            all_child_d.append(child_d)
        all_child_h.sort(reverse = True)
        all_child_d.sort(reverse = True)
        
        if len(all_child_h) == 0:
            return 1, 0
        
        if len(all_child_h) == 1:
            max_h = all_child_h[0] + 1
            max_d = max(all_child_d[0], all_child_h[0])
        else:
            max_h = all_child_h[0] + 1
            max_d = max(all_child_d[0], all_child_h[0] + all_child_h[1])
        return max_h, max_d
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

