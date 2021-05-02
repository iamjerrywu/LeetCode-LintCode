# Closest Binary Search Tree Value II 901 \(H\)

## Problem

Given a non-empty binary search tree and a target value, find `k` values in the BST that are closest to the target.

* Given target value is a floating point.
* You may assume `k` is always valid, that is: `k ≤ total` nodes.
* You are guaranteed to have only one `unique` set of k values in the BST that are closest to the target.

Have you met this question in a real interview?  YesProblem Correction

#### Example

**Example 1:**

```text
Input:
{1}
0.000000
1
Output:
[1]
Explanation：
Binary tree {1},  denote the following structure:
 1
```

**Example 2:**

```text
Input:
{3,1,4,#,2}
0.275000
2
Output:
[1,2]
Explanation：
Binary tree {3,1,4,#,2},  denote the following structure:
  3
 /  \
1    4
 \
  2
```

#### Challenge

Assume that the BST is balanced, could you solve it in less than O\(n\) runtime \(where n = total nodes\)?

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
    def closestKValues(self, root, target, k):
        results = []
        if root is None or k == 0:
            return results
        next_stack, prev_stack = self.get_stacks(root, target)
        
        for _ in range(k):
            if len(next_stack) == 0 and len(prev_stack) == 0:
                break
            next_diff = sys.maxsize if len(next_stack) == 0 else abs(next_stack[-1].val - target)
            prev_diff = sys.maxsize if len(prev_stack) == 0 else abs(prev_stack[-1].val - target)
            
            if next_diff < prev_diff:
                results.append(self.get_next(next_stack))
            else:
                results.append(self.get_prev(prev_stack))
                
        return results
    
    def get_stacks(self, root, target):
        next_stack, prev_stack = [], []
        while root:
            if root.val < target:
                prev_stack.append(root)
                root = root.right
            else:
                next_stack.append(root)
                root = root.left
                
        return next_stack, prev_stack
    
    def get_next(self, next_stack):
        value = next_stack[-1].val
        node = next_stack.pop().right 
        while node:
            next_stack.append(node)
            node = node.left
            
        return value
        
    def get_prev(self, prev_stack):
        value = prev_stack[-1].val
        node = prev_stack.pop().left     
        while node:
            prev_stack.append(node)
            node = node.right
            
        return value
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

