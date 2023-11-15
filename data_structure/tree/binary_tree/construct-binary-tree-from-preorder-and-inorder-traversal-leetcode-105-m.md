# Construct Binary Tree from Preorder and Inorder Traversal (LeetCode 105) (M)

## Problem

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return _the binary tree_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

<pre><code><strong>Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
</strong><strong>Output: [3,9,20,null,null,15,7]
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: preorder = [-1], inorder = [-1]
</strong><strong>Output: [-1]
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= preorder.length <= 3000`
* `inorder.length == preorder.length`
* `-3000 <= preorder[i], inorder[i] <= 3000`
* `preorder` and `inorder` consist of **unique** values.
* Each value of `inorder` also appears in `preorder`.
* `preorder` is **guaranteed** to be the preorder traversal of the tree.
* `inorder` is **guaranteed** to be the inorder traversal of the tree.



## Solution



<figure><img src="../../../.gitbook/assets/Screenshot 2023-11-15 at 12.30.00 AM.png" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Python" %}
```python
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() == 0 or inorder.size() == 0) return NULL;

        TreeNode* root = new TreeNode(preorder[0]);
        int mid = find_idx(inorder, preorder[0]);
        
        vector<int> left_pre = sub_vec(preorder, 1, mid + 1);
        vector<int> left_in = sub_vec(inorder, 0, mid);
        root->left = buildTree(left_pre, left_in);
        vector<int> right_pre = sub_vec(preorder, mid + 1, preorder.size());
        vector<int> right_in = sub_vec(inorder, mid + 1, inorder.size());
        
        root->right = buildTree(right_pre, right_in);
        
        return root;
    }

private:
    int find_idx(vector<int>& inorder, int tar) {
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == tar) return i;
        }
        return 0;
    }

    vector<int> sub_vec(vector<int>& vec, int s, int e) {
        vector<int> ret;
        for (int i = s; i < e; i++) {
            ret.push_back(vec[i]);
        }
        return ret;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
