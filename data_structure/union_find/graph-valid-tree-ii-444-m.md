# Graph Valid Tree II 444 \(M\)

## Problem



Please design a data structure which can do the following operations:

* `void addEdge(int a, int b)`:add an edge between node aa and node bb. It is guaranteed that there isn't self-loop or multi-edge.
* `bool isValidTree()`: Check whether these edges make up a valid tree.

Example

**Example 1**

```text
Input:addEdge(1, 2)isValidTree()addEdge(1, 3)isValidTree()addEdge(1, 5)isValidTree()addEdge(3, 5)isValidTree()Output: ["true","true","true","false"]
```

## Solution 

If this problem is solved using BFS, then the time complexity would be too large.

* If called `isValidTree()` m times, then time complexity would be O\(m \* \(N + E\)\)

Therefore, should use UnionFind in this case

### Code - Union Find

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

