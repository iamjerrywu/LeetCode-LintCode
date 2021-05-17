# Binary Tree Level Sum 482 \(E\)

## Problem

Description

Given a binary tree and an integer which is the depth of the target level.

Calculate the sum of the nodes in the target level.Example

**Example 1:**

```text
Input：{1,2,3,4,5,6,7,#,#,8,#,#,#,#,9},2
Output：5 
Explanation：
     1
   /   \
  2     3
 / \   / \
4   5 6   7
   /       \
  8         9
2+3=5
```

**Example 2:**

```text
Input：{1,2,3,4,5,6,7,#,#,8,#,#,#,#,9},3
Output：22
Explanation：
     1
   /   \
  2     3
 / \   / \
4   5 6   7
   /       \
  8         9
4+5+6+7=22
```

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

from queue import Queue

class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """

    def levelSum(self, root, level):
        # write your code here
        queue = Queue()
        res = 0
        cur_level = 0
        if not root:
            return res
        queue.put(root)
        cur_level+=1
        while not queue.empty():
            for i in range(queue.qsize()):
                cur = queue.get()
                if cur_level == level:
                    res+=cur.val
                    continue
                if cur.left:
                    queue.put(cur.left)
                if cur.right:
                    queue.put(cur.right)
            cur_level+=1
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

