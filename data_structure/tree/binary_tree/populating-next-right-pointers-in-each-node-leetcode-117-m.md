# Populating Next Right Pointers in Each Node (LeetCode 117) (M)

## Problem

Given a binary tree

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

**Example 1:**![](https://assets.leetcode.com/uploads/2019/02/15/117\_sample.png)

```
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

**Example 2:**

```
Input: root = []
Output: []
```

**Constraints:**

* The number of nodes in the tree is in the range `[0, 6000]`.
* `-100 <= Node.val <= 100`

**Follow-up:**

* You may only use constant extra space.
* The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

## Solution - Level Traversal

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

{% tab title="C++" %}
```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (root == NULL)
            return root;
        deque<Node*> dq;
        
        dq.push_back(root);
        bfs(dq);
        return root;
    }
    
    void bfs(deque<Node*> dq) {
        while (!dq.empty()) {
            Node* prev = NULL;
            int size = dq.size();
            for (int i = 0; i < size; i++) {
                Node* cur = dq.front();
                dq.pop_front();
                if (prev != NULL) {
                    prev->next = cur;
                }
                if (cur->left != NULL) {
                    dq.push_back(cur->left);
                }
                if (cur->right != NULL) {
                    dq.push_back(cur->right);
                }
                prev = cur;
            }
        }
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**&#x20;



## Solution - Constant Space

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**&#x20;
