# Construct String from Binary Tree 1137 \(E\)

## Problem

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "\(\)". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.Have you met this question in a real interview?  YesProblem Correction

#### Example

**Example 1:**

```text
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
```

**Example 2:**

```text
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
```

## Solution - Stright Forward Search

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
    @param t: the root of tree
    @return: return a string
    """
    def tree2str(self, t):
        # write your code here
        res = ['']
        
        right_exist = True if t.right else False
        self.helper(t, res, right_exist)
        return res[0][1:-1]
    
    def helper(self, node, res, right_exist):
        if not node:
            if right_exist:
                res[0]+="()"
            return 
        res[0]+='(' + str(node.val)
        right_exist = True if node.right else False
        self.helper(node.left, res, right_exist)
        right_exist = False
        self.helper(node.right, res, right_exist)
        res[0]+=')'
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(h\)**
* **Space Complexity:**

## Solution - Stright Forward Search



