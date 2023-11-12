# Validate Binary Search Tree 95 (M)

## Problem



Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

* The left subtree of a node contains only nodes with keys **less than** the node's key.
* The right subtree of a node contains only nodes with keys **greater than** the node's key.
* Both the left and right subtrees must also be binary search trees.
* A single node tree is a BST

Example

**Example 1:**

```
Input:  {-1}
Output：true
Explanation：
For the following binary tree（only one node）:
	      -1
This is a binary search tree.
```

**Example 2:**

```
Input:  {2,1,4,#,#,3,5}
Output: true
For the following binary tree:
	  2
	 / \
	1   4
	   / \
	  3   5
This is a binary search tree.
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

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def __init__(self):
        self.res = []
    
    def isValidBST(self, root):
        # write your code here
        self.inorder_traverse(root)
        for i in range(1, len(self.res)):
            if self.res[i]<= self.res[i - 1]:
                return False
        return True
    
    def inorder_traverse(self, root):
        if not root:
            return 
        self.inorder_traverse(root.left)
        self.res.append(root.val)
        self.inorder_traverse(root.right)
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



## Solution - Recursion with Boundary

{% tabs %}
{% tab title="Python" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float(-inf), float('inf'))
        
    def dfs(self, node, low, high):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        
        return self.dfs(node.left, low, node.val) and self.dfs(node.right, node.val, high)
    
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return dfs(root, LONG_MIN, LONG_MAX);
    }

private:
    static bool dfs(TreeNode* root, long left_b, long right_b) {
        if (root == NULL) return true;
        if (root->val >= right_b or root->val <= left_b) return false;
        return dfs(root->left, left_b, root->val) and dfs(root->right, root->val, right_b);
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
