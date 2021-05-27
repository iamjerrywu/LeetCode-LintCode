# Symmetric Tree 1360 \(M\)

## Problem

Given a binary tree, check whether it is a mirror of itself \(ie, symmetric around its center\).Example

**Example1**

```text
Input: {1,2,2,3,4,4,3}Output: trueExplanation:    1   / \  2   2 / \ / \3  4 4  3This binary tree {1,2,2,3,4,4,3} is symmetric
```

**Example2**

```text
Input: {1,2,2,#,3,#,3}Output: falseExplanation:    1   / \  2   2   \   \   3    3This is not a symmetric tree
```

Challenge

Could you solve it both recursively and iteratively?

## Solution - BFS

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
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True

        queue = [root]
        while queue:
            next_queue = []
            for i in range(len(queue)):
                if not queue[i]:
                    continue                                                                                        
                next_queue.append(queue[i].left)
                next_queue.append(queue[i].right)
            if not self.is_mirror(next_queue):
                return False
            queue = next_queue
        return True
    
    def is_mirror(self, queue):
        left, right = 0, len(queue) - 1
        while left < right:
            if not self.is_same(queue[left], queue[right]):
                return False
            left+=1
            right-=1
        return True
    
    def is_same(self, node1, node2):
        if node1 and node2:
            return node1.val == node2.val

        return not node1 and not node2
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n/2\)**
  * Each pair \(left, right\) node would be traversed, and each node only be traversed once
* **Space Complexity:**

\*\*\*\*

## Solution - Recursion DFS

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
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
        return self._is_symmetric(root.left, root.right)
    
    def _is_symmetric(self, left_root, right_root):
        if not left_root and not right_root:
            return True
        if not left_root or not right_root:
            return False
        if left_root.val != right_root.val:
            return False
        
        # WARNING!
        # the symmetric policy!
        # left_root.left <-> right_root.right
        # left_root.right <-> right_root.left
        left_symmetric = self._is_symmetric(left_root.left, right_root.right)
        right_symmetric = self._is_symmetric(left_root.right, right_root.left)

        return left_symmetric and right_symmetric
        


```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n/2\)**
  * Each pair \(left, right\) node would be traversed, and each node only be traversed once
* **Space Complexity:**

\*\*\*\*

## Solution - Iteration DFS

To ensure a tree's structure:

* Preorder traversal + inorder traversal
* Postorder traversal + inorder traversal

{% hint style="danger" %}
Preordere + Postorder traversal cannot ensure tree's structure
{% endhint %}

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
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
        inorder = self.inorder(root, reverse = False)
        reverse_inorder = self.inorder(root, reverse = True)
        if inorder != reverse_inorder:
            return False
        
        preorder = self.preorder(root, reverse = False)
        reverse_preorder = self.preorder(root, reverse = True)

        return preorder == reverse_preorder
    
    def preorder(self, root, reverse):
        stack = [root]
        order = []

        while stack:
            node = stack.pop()
            order.append(node.val)
            right = self.get_right(node, reverse)
            if right:
                stack.append(right)
            left = self.get_left(node, reverse)
            if left:
                stack.append(left)
        return order
    
    def inorder(self, root, reverse):
        stack = []
        while root:
            stack.append(root)
            root = self.get_left(root, reverse)
        
        order = []
        while stack:
            node = stack[-1]
            order.append(node.val)
            
            right = self.get_right(node, reverse)
            if right:
                node = right
                while node:
                    stack.append(node)
                    node = self.get_left(node, reverse)
            else:
                node = stack.pop()
                while stack and self.get_right(stack[-1], reverse) == node:
                    node = stack.pop()
        return order 

    def get_left(self, node, reverse):
        if reverse:
            return node.right
        return node.left
    
    def get_right(self, node, reverse):
        if reverse:
            return node.left
        return node.right
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(4n\)**
  * Traverse 4 times
* **Space Complexity:**

