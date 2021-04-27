# Minimum Subtree 596 \(E\)

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

DFS \(post-order traversal\) using divide and conquer, traversing all the subtree and return the current root tree's min subtree sum, min subtree node and root weight

### Algorithm

Recursion and calculate the current root's total weight by summing the weight from left/right subtree, then return the right values

#### Step by step 

* Recursion input the root and return that root's tree's weight, minimum subtree weight sum and node
* Calculate the weight from left/right subtree, then get the current root's tree's weight by adding root's value
  * Compare the between left subtree weight, right subtree weight and current root tree's weight, depend what values should be returned

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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def __init__(self):
        self.minimum_weight = float('inf')
        self.minimum_subtree_root = None
    
    def findSubtree(self, root):
        # write your code here
        self.get_tree_sum(root)
        return self.minimum_subtree_root
    
    def get_tree_sum(self, root):
        if root is None:
            return 0
        
        left_weight = self.get_tree_sum(root.left)
        right_weight = self.get_tree_sum(root.right)
        root_weight = left_weight + right_weight + root.val
        
        if root_weight < self.minimum_weight:
            self.minimum_subtree_root = root
            self.minimum_weight = root_weight
        return root_weight
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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        _, min_node, _ = self.helper(root)
        return min_node
    
    def helper(self, root):
        if not root:
            return float('inf'), None, 0
        
        left_min_weight, left_min_node, left_sum = self.helper(root.left)
        right_min_weight, right_min_node, right_sum = self.helper(root.right)
        cur_sum = left_sum + right_sum + root.val
        
        if left_min_weight == min(left_min_weight, right_min_weight, cur_sum):
            return left_min_weight, left_min_node, cur_sum
        if right_min_weight == min(left_min_weight, right_min_weight, cur_sum):
            return right_min_weight, right_min_node, cur_sum
        return cur_sum, root, cur_sum

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time complexity: O\(n\)**
  * Traverse all nodes 
* **Space Complexity: O\(1\)**
  * Constant space complexity 

