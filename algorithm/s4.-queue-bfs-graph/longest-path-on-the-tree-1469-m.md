# Longest Path On The Tree 1469 \(M\)

## Problem

Given a tree consisting of `n` nodes, `n-1` edges. Output the distance between the two nodes with the furthest distance on this tree.  
Given three arrays of size `n-1`, `starts`, `ends`, and `lens`, indicating that the `i`-th edge is from `starts[i]` to `ends[i]` and the length is `lens[i]`.

Return the farthest distance between any two nodes on the tree, not the depth of the tree. Note that the given edges are undirected edge.  
It is guaranteed that the given edges are able to constitute a tree.

* 1 \leq n \leq 1\* 10^51≤n≤1∗10​5​​
* 1 \leq lens\[i\] \leq 1\* 10^31≤lens\[i\]≤1∗10​3​​

Example

**Example 1:**

```text
Input：n=5,starts=[0,0,2,2],ends=[1,2,3,4],lens=[1,2,5,6]
Output：11
Explanation:
(3→2→4)the length of this path is `11`,as well as(4→2→3)。
```

**Example 2:**

```text
Input：n=5,starts=[0,0,2,2],ends=[1,2,3,4],lens=[5,2,5,6]
Output：13
Explanation:
(1→0→2→4)the length of this path is`13`,as well as(4→2→0→1)。
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

