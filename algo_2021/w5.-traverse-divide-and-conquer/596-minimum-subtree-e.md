# 596 Minimum Subtree \(E\)

## Problem

[https://www.lintcode.com/problem/596](https://www.lintcode.com/problem/596)

### Description

Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

{% hint style="info" %}
LintCode will print the subtree which root is your return node. It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.
{% endhint %}

### Example

Example 1:

```text
Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5 
The sum of whole tree is minimum, so return the root.
```

Example 2:

```text
Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
```

## Approach - DFS \(Divide and Conquer \)

### Intuition

Get left/right sub-tree's height recursively and judge if they are balanced or not

### Algorithm

Recursion to get left/right subtree's height respectively, and calculate the root height from left/right subtrees's height

#### Step by step 

* Recursion to return 
  * if\_balanced: if that root tree is balanced
  * height: that root tree's height, calculated based on max of height from left/right trees
* In recursion, eventually can get the whole tree returned values

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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        is_balanced, _ = self.validate(root)
        return is_balanced
    
    def validate(self, root):
        # if empty tree, it's balanced and return heigh = 0
        if not root:
            return True, 0
        
        is_left_balanced, left_height = self.validate(root.left)
        is_right_balanced, right_height = self.validate(root.right)
        root_height = max(left_height, right_height) + 1

        if not is_left_balanced or not is_right_balanced: 
            return False, root_height
        if abs(left_height - right_height) > 1:
            return False, root_height
        return True, root_height
        

```
{% endtab %}

{% tab title="java" %}
```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */


public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if this Binary tree is Balanced, or false.
     */
    class Res {
    public boolean isBalanced;
    public int height;
    public Res(boolean isBalanced, int height) {
        this.isBalanced = isBalanced;
        this.height = height;
    }
}
    
    public boolean isBalanced(TreeNode root) {
        // write your code here
        Res result= validate(root);
        return result.isBalanced;
    }

    private Res validate(TreeNode root) {
        if (root == null) {
            return new Res(true, 0);
        }

        Res leftRes = validate(root.left);
        Res rightRes = validate(root.right);
        int rootHeight = Math.max(leftRes.height, rightRes.height) + 1;

        if (!leftRes.isBalanced || !rightRes.isBalanced) {
            return new Res(false, rootHeight);
        }
        if (Math.abs(leftRes.height - rightRes.height) > 1) {
            return new Res(false, rootHeight);
        }
        return new Res(true, rootHeight);
        
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time complexity: O\(n\)**
  * Traverse all nodes 
* **Space Complexity: O\(1\)**
  * Constant space complexity 

