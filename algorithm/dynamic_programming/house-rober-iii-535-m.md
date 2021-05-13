# House Rober III 535 \(M\)

## Problem

After robbing a street and a circle of houses last time, the burglar found a new place to rob. **But this time, the area composed of all the houses is strange. After investigating the terrain, the clever burglar found that the terrain this time is a binary tree.** Similar to the previous two thefts, each house had a certain amount of money in it. **The only constraint you face is that adjacent houses are equipped with interconnected anti-theft systems, which will automatically alarm when two adjacent houses are robbed on the same day.**

Calculate how much money you can get if you rob tonight, without touching the alarm.

This is an extension of [House Robber](http://www.lintcode.com/problem/house-robber/) and [House Robber II](http://www.lintcode.com/problem/house-robber-ii/), but this time the terrain has changed from straight lines and circles to binary trees.Example

**Example1**

```text
Input: {3,2,3,#,3,#,1}
Output: 7
Explanation:
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
3
/ \
2 3
\ \
3 1
```

**Example2**

```text
Input: {3,4,5,1,3,#,1}
Output: 9
Explanation:
Maximum amount of money the thief can rob = 4 + 5 = 9.
3
/ \
4 5
/ \ \
1 3 1
```

## Solution - DP

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
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        # write your code here
        rob, not_rob = self.visit(root)
        return max(rob, not_rob)
    
    def visit(self, root):
        if not root:
            return 0, 0
        left_rob, left_not_rob = self.visit(root.left)
        right_rob, right_not_rob = self.visit(root.right)

        rob = root.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)

        return rob, not_rob

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

