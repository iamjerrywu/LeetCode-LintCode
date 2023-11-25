# Page

## Problem

Given the `root` of a binary search tree, and an integer `k`, return _the_ `kth` _smallest value (**1-indexed**) of all the values of the nodes in the tree_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

<pre><code><strong>Input: root = [3,1,4,null,2], k = 1
</strong><strong>Output: 1
</strong></code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

<pre><code><strong>Input: root = [5,3,6,2,4,null,null,1], k = 3
</strong><strong>Output: 3
</strong></code></pre>

&#x20;

**Constraints:**

* The number of nodes in the tree is `n`.
* `1 <= k <= n <= 104`
* `0 <= Node.val <= 104`

&#x20;

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?



## Solution

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
````cpp
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
    int kthSmallest(TreeNode* root, int k) {
        int ans, cnt = 0;
        preorder(root, cnt, ans, k);
        return ans;
    }

private:
    void preorder(TreeNode* node, int &cnt, int &ans, int k) {
        if (node == NULL) return;
        preorder(node->left, cnt, ans, k);
        if (cnt == k - 1) ans = node->val;
        cnt++;
        
        preorder(node->right, cnt, ans, k);
    }
};
```
````
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
