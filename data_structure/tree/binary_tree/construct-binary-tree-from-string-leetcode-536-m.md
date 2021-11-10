# Construct Binary Tree from String (LeetCode 536) (M)



## Problem

&#x20;

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the **left** child node of the parent first if it exists.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/02/butree.jpg)

```
Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
```

**Example 2:**

```
Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]
```

**Example 3:**

```
Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
```

&#x20;

**Constraints:**

* `0 <= s.length <= 3 * 104`
* `s` consists of digits, `'('`, `')'`, and `'-'` only.

## Solution

![](<../../../.gitbook/assets/Screen Shot 2021-10-23 at 6.10.56 PM.png>)

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
    def str2tree(self, s: str) -> Optional[TreeNode]:
        return self.dfs(s)
    
    def dfs(self, cur_s):
        if not cur_s:
            return 
        n = len(cur_s)
        left_tree_start = 0
        left_tree_end = 0
        left_tree_start = cur_s.find('(')
        if left_tree_start == -1:
            return TreeNode(int(cur_s))
        
        root = TreeNode(int(cur_s[:left_tree_start]))
        # find when the left tree end
        left_parenthesis_cnt = 0
        for i in range(left_tree_start, n):
            if cur_s[i] == '(':
                left_parenthesis_cnt+=1
            elif cur_s[i] == ')':
                left_parenthesis_cnt-=1
            if left_parenthesis_cnt == 0:
                left_tree_end = i
                break
        root.left = self.dfs(cur_s[left_tree_start + 1:left_tree_end])
        root.right = self.dfs(cur_s[left_tree_end + 2: n - 1])
        return root
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity:O(n)**
