# Flatten Binary Tree to Linked List 453 (E)

## Problem

Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the _right_ pointer in TreeNode as the _next_ pointer in ListNode.

Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.Example

**Example 1:**

```
Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
```

**Example 2:**

```
Input:{1}
Output:{1}
Explanation：
         1
         1
```

Challenge

Do it in-place without any extra memory.

## Solution - Divide Conquer (Wrong Example using Global variable)

### Code

{% hint style="danger" %}
Following case would lead to error, since using global variable, might change the root.right value
{% endhint %}

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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    prev_node = None
    def flatten(self, root):
        # write your code here
        if not root:
            return 
        
        if self.prev_node:
            self.prev_node.left = None
            self.prev_node.right = root
        
        self.prev_node = root
        self.flatten(root.left)
        # here the root.right might be modified due to global variable: self.prev_node.right
        self.flatten(root.right)

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

## Solution - Divide Conquer

### Code

![](<../../../.gitbook/assets/Screen Shot 2021-04-22 at 12.27.58 AM.png>)

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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.flatten_and_return_last_node(root)
    
    def flatten_and_return_last_node(self, root):
        if not root:
            return None
        
        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)

        # connect
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        # in-order to return right_last -> left_last -> root
        return right_last or left_last or root

```
{% endtab %}

{% tab title="Python (Better)" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def flatten(self, root):
        
        node, last_node = self.dfs(root)
        return node
    
    
    def dfs(self, node):
        if not node:
            return None, None
        left, left_last = self.dfs(node.left)
        right, right_last = self.dfs(node.right)
        
        node.left = None
        last = node
        if left:
            last.right = left
            last = left_last
        if right:
            last.right = right
            last = right_last
        return node, last
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

