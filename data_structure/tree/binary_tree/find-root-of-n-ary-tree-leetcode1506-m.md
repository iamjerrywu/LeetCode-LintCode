# Find Root of N-Ary Tree (LeetCode1506) (M)



## Problem

****

You are given all the nodes of an [**N-ary tree**](https://leetcode.com/articles/introduction-to-n-ary-trees/) as an array of `Node` objects, where each node has a **unique value**.

Return _the **root** of the N-ary tree_.

**Custom testing:**

An N-ary tree can be serialized as represented in its level order traversal where each group of children is separated by the `null` value (see examples).

![](https://assets.leetcode.com/uploads/2019/11/08/sample\_4\_964.png)

For example, the above tree is serialized as `[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`.

The testing will be done in the following way:

1. The **input data** should be provided as a serialization of the tree.
2. The driver code will construct the tree from the serialized input data and put each `Node` object into an array **in an arbitrary order**.
3. The driver code will pass the array to `findRoot`, and your function should find and return the root `Node` object in the array.
4. The driver code will take the returned `Node` object and serialize it. If the serialized value and the input data are the **same**, the test **passes**.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

<pre><code>Input: tree = [1,null,3,2,4,null,5,6]
<strong>Output:
</strong> [1,null,3,2,4,null,5,6]
<strong>Explanation:
</strong> The tree from the input data is shown above.
The driver code creates the tree and gives findRoot the Node objects in an arbitrary order.
For example, the passed array could be [Node(5),Node(4),Node(3),Node(6),Node(2),Node(1)] or [Node(2),Node(6),Node(1),Node(3),Node(5),Node(4)].
The findRoot function should return the root Node(1), and the driver code will serialize it and compare with the input data.
The input data and serialized Node(1) are the same, so the test passes.</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/11/08/sample\_4\_964.png)

<pre><code>Input: tree = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>Output:
</strong> [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]</code></pre>

&#x20;

**Constraints:**

* The total number of nodes is between `[1, 5 * 104]`.
* Each node has a **unique** value.

&#x20;

**Follow up:**

* Could you solve this problem in constant space complexity with a linear time algorithm?



## Solution - Set

{% tabs %}
{% tab title="Python" %}
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        seen = set()
        for node in tree:
            for child in node.children:
                seen.add(child)
        for node in tree:
            if node not in seen:
                return node
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

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - Constant Space

{% tabs %}
{% tab title="Python" %}
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        sum_val = 0
        for node in tree:
            sum_val+=node.val
            for child in node.children:
                sum_val-=child.val
        for node in tree:
            if node.val == sum_val:
                return node
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

* **Time Complexity:**
* **Space Complexity:**
