# Flatten Binary Tree to Linked List 453 \(E\)

## Problem

Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the _right_ pointer in TreeNode as the _next_ pointer in ListNode.

Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.Example

**Example 1:**

```text
Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
```

**Example 2:**

```text
Input:{1}
Output:{1}
Explanation：
         1
         1
```

Challenge

Do it in-place without any extra memory.

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python

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

