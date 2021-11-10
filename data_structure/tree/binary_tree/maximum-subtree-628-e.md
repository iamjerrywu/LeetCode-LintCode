# Maximum Subtree 628 (E)

## Problem

Description

Given a binary tree, find the subtree with maximum sum. Return the root of the subtree.

LintCode will print the node you return as the optimal subtree.\
It's guaranteed that there is only one subtree with maximum sum and the given binary tree is not an empty tree.Example

Example 1:

```
Input:
{1,-5,2,0,3,-4,-5}
Output:3
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
0   3 -4  -5
The sum of subtree 3 (only one node) is the maximum. So we return 3.
```

Example 2:

```
Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
```

## Solution - Global Variable

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
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        self.max_sum = -float('inf')
        self.max_node = root
        self.dfs(root)
        return self.max_node
    
    def dfs(self, node):
        if not node:
            return 0
        left_s = self.dfs(node.left)
        right_s = self.dfs(node.right)
        s = left_s + right_s + node.val

        if self.max_sum < s:
            self.max_sum = s
            self.max_node = node
        return s       
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

****

## Solution - DC (w/o Global Variable)

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
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        if not root:
            return None
        _, _, node = self.dc(root)
        return node
    def dc(self, node):
        if not node:
            return 0, 0, node
        
        left_sum, left_max, left_max_node = self.dc(node.left)
        right_sum, right_max, right_max_node = self.dc(node.right)
        # if root 
        if left_sum == 0 and right_sum == 0:
            return node.val, node.val, node
        else:
            total_sum = node.val + left_sum + right_sum
            if total_sum > right_max and total_sum > left_max:
                return total_sum, total_sum, node
            elif left_max > total_sum and left_max > right_max:
                return total_sum, left_max, left_max_node
            else:
                return total_sum, right_max, right_max_node   
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
