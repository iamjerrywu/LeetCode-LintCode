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

{% hint style="warning" %}
For a tree there's O\(n\) amounts of subtrees
{% endhint %}

## Approach - DC With Global Variable

### Intuition

DFS \(post-order traversal\) using divide and conquer, traversing all the subtree and record the minimum sum and node in global variable 

### Algorithm

Recursion and calculate the current root's total weight by summing the weight from left/right subtree, then compare to global min values

#### Step by step 

* Recursion input the root and return that root's tree's weight
* Calculate the weight from left/right subtree, then get the current root's tree's weight by adding root's value
  * Compare the root's weight with global variable minimum\_weight, then update the global variable 

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
     * @param root: the root of binary tree
     * @return: the root of the minimum subtree
     */
    private int minSum;
    private TreeNode minRoot;
    public Solution() {
       minSum = Integer.MAX_VALUE;
       minRoot = null; 
    }
    public TreeNode findSubtree(TreeNode root) {
        // write your code here
        getSum(root);
        
        return minRoot;
    }

    private int getSum(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftWeight = getSum(root.left);
        int rightWeight = getSum(root.right);
        int rootWeight = leftWeight + rightWeight + root.val;

        if (rootWeight < minSum) {
            minSum = rootWeight;
            minRoot = root;
        }
        return rootWeight;
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



## Approach - DC Without Global Variable

### Intuition

DFS \(post-order traversal\) using divide and conquer, traversing all the subtree and record the minimum sum and node in global variable 

### Algorithm

Recursion and calculate the current root's total weight by summing the weight from left/right subtree, then compare to global min values

#### Step by step 

* Recursion input the root and return that root's tree's weight
* Calculate the weight from left/right subtree, then get the current root's tree's weight by adding root's value
  * Compare the root's weight with global variable minimum\_weight, then update the global variable 

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
     * @param root: the root of binary tree
     * @return: the root of the minimum subtree
     */
    private int minSum;
    private TreeNode minRoot;
    public Solution() {
       minSum = Integer.MAX_VALUE;
       minRoot = null; 
    }
    public TreeNode findSubtree(TreeNode root) {
        // write your code here
        getSum(root);
        
        return minRoot;
    }

    private int getSum(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftWeight = getSum(root.left);
        int rightWeight = getSum(root.right);
        int rootWeight = leftWeight + rightWeight + root.val;

        if (rootWeight < minSum) {
            minSum = rootWeight;
            minRoot = root;
        }
        return rootWeight;
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

