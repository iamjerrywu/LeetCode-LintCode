# Binary Tree Preorder Traversal 66 (E)

## Problem

Description

Given a binary tree, return the preorder traversal of its nodes' values.

* The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
* The number of nodes does not exceed 20.

Example

**Example 1:**

Input:

```
binary tree = {1,2,3}
```

Output:

```
[1,2,3]
```

Explanation:

&#x20;  1\
&#x20; /  \\\
2     3\
It will be serialized as {1,2,3} preorder traversal

**Example 2:**

Input:

```
binary tree = {1,#,2,3}
```

Output:

```
[1,2,3]
```

Explanation:

1\
&#x20; \\\
&#x20;  2\
&#x20; /\
3\
It will be serialized as {1,#,2,3} preorder traversalChallenge

Can you do it without recursion?

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
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        res = []
        self.helper(root, res)
        return res
    def helper(self,node, res):
        if not node:
            return
        res.append(node.val)
        self.helper(node.left, res)
        self.helper(node.right, res)


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
    vector<int> preorderTraversal(TreeNode* root) {
        // node -> left -> right 
        vector<int> res;
        dfs(root, res);
        return res;
    }

private:
    void dfs(TreeNode* node, vector<int> &res) {
        if (node == nullptr) return;
        res.push_back(node->val);
        dfs(node->left, res);
        dfs(node->right, res);
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(h)**



## Solution - Iteration using Stack

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
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        stack = [root]
        preorder = []

        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

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
    vector<int> preorderTraversal(TreeNode* root) {
        stack<TreeNode*> s;
        s.push(root);
        vector<int> res;

        while(!s.empty()) {
            TreeNode* curr = s.top();
            s.pop();
            if (curr != nullptr) {
                res.push_back(curr->val);
                // push right
                s.push(curr->right);
                // push left 
                s.push(curr->left);
            }
        }
        return res;
        
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(h)**

