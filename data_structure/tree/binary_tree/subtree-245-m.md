# Subtree 245 \(M\)

## Problem

You have two very large binary trees: `T1`, with millions of nodes, and `T2`, with hundreds of nodes. Create an algorithm to decide if `T2` is a subtree of `T1`.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.Example

**Example 1:**

```text
Input：{1,2,3,#,#,4},{3,4}
Output：true
Explanation：
T2 is a subtree of T1 in the following case:
           1                3
          / \              / 
    T1 = 2   3      T2 =  4
            /
           4
```

**Example 2:**

```text
Input：{1,2,3,#,#,4},{3,#,4}
Output：false
Explanation：
T2 isn't a subtree of T1 in the following case:

           1               3
          / \               \
    T1 = 2   3       T2 =    4
            /
           4
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

