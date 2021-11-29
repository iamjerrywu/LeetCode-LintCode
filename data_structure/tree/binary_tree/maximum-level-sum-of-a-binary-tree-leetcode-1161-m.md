# Maximum level Sum of a Binary Tree (LeetCode 1161) (M)

## Problem

Given the `root` of a binary tree, the level of its root is `1`, the level of its children is `2`, and so on.

Return the **smallest** level `x` such that the sum of all the values of nodes at level `x` is **maximal**.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/05/03/capture.JPG)

```
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
```

**Example 2:**

```
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
```

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 104]`.
* `-105 <= Node.val <= 105`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        queue = collections.deque([root])
        max_sum = -float('inf')
        max_sum_level = 1
        level = 1
        while queue:
            sum_val = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum_val+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum_val > max_sum:
                max_sum = sum_val
                max_sum_level = level
            level+=1
        return max_sum_level
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
