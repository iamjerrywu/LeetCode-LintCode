# Populating Next Right Pointers in Each Node (LeetCode 116) (M)

## Problem

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

**Example 1:**![](https://assets.leetcode.com/uploads/2019/02/14/116\_sample.png)

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

**Example 2:**

```
Input: root = []
Output: []
```

**Constraints:**

* The number of nodes in the tree is in the range `[0, 212 - 1]`.
* `-1000 <= Node.val <= 1000`

**Follow-up:**

* You may only use constant extra space.
* The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

## Solution - Level Order Traversal

{% tabs %}
{% tab title="Python" %}
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        queue = collections.deque()
        queue.append(root)
        prev = None
        res = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i != 0:     
                    prev.next = node
                prev = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            prev.next = None
        return root
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:  O(n)**
* **Space Complexity: O(n)**

****

## Solution - Constant Space

**Intuition**

Let's look at the two types of `next` pointer connections we need to establish for a given tree.

1.  This first case is the one where we establish the next pointers between the two children of a given node. This is the easier of the two cases since both the children are accessible via the same node. We can simply do the following to establish this connection.

    ```
     node.left.next = node.right
    ```

    ![](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/Figures/116/img6.png)
2. This next case is not too straightforward to handle. In addition to establishing the next pointers between the nodes having a common parent, we also need to set-up the correct pointers between nodes which have a different parent.![](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/Figures/116/img7.png)

If we simply had the parent pointers available with each node, this problem would have been trivial to solve. However, we don't have any such pointers available. The basic idea for this approach is based on the fact that:



{% tabs %}
{% tab title="Python" %}
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        left_most = root
        while left_most.left:
            head = left_most
            while head:
                head.left.next = head.right
                
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            left_most = left_most.left
        return root
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: **
* **Space Complexity: **
