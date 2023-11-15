# Sum Root to Leaf Numbers (LeetCode 129) (M)

## Problem



You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

* For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return _the total sum of all root-to-leaf numbers_. Test cases are generated so that the answer will fit in a **32-bit** integer.

A **leaf** node is a node with no children.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)

```
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg)

```
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

&#x20;

**Constraints:**

* The number of nodes in the tree is in the range `[1, 1000]`.
* `0 <= Node.val <= 9`
* The depth of the tree will not exceed `10`.



## Solution&#x20;

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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, "")
        
    
    def dfs(self, node, tmp):
        ans = 0
        if not node.left and not node.right:
            ans+=int(tmp + str(node.val))
            return ans
        tmp = tmp + str(node.val)
        if node.left:
            ans += self.dfs(node.left, tmp)
        
        if node.right:
            ans +=self.dfs(node.right, tmp)
        return ans
    
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(h)**
  * **h: height of the binary tree**
* **Space Complexity:**

