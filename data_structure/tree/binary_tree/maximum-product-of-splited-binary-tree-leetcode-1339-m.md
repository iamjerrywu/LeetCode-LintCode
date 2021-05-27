# Maximum Product of Splited Binary Tree \(LeetCode 1339\) \(M\)

## Problem

Given a binary tree `root`. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.

Since the answer may be too large, return it modulo 10^9 + 7.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png)

```text
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/01/21/sample_2_1699.png)

```text
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
```

**Example 3:**

```text
Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
```

**Example 4:**

```text
Input: root = [1,1]
Output: 1
```

**Constraints:**

* Each tree has at most `50000` nodes and at least `2` nodes.
* Each node's value is between `[1, 10000]`.

## Solution - DFS

### Code

{% tabs %}
{% tab title="python" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        subtree_sums = []
        total_sum = self.get_subtree_sum(root, subtree_sums)
        
        ans = 0
        for subtree_sum in subtree_sums:
            ans = max(ans, subtree_sum * (total_sum - subtree_sum))
        
        return ans%(10**9 + 7)
    
    def get_subtree_sum(self, node, subtree_sums):
        if not node:
            return 0
        left_sum = self.get_subtree_sum(node.left, subtree_sums)
        right_sum = self.get_subtree_sum(node.right, subtree_sums)
        cur_sum = left_sum + right_sum + node.val
        subtree_sums.append(cur_sum)
        return cur_sum
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(2n\)**
  * 1st traverse to find all subtree sum: O\(n\)
  * Later find max of product O\(n\)
* **Space Complexity: O\(n\)**

