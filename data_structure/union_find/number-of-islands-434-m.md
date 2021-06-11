# Number of Islands II 434 \(M\)

## Problem

Given a n,m which means the row and column of the 2D matrix and an array of pair A\( size k\). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A\[i\].x, A\[i\].y means that you can change the grid matrix\[A\[i\].x\]\[A\[i\].y\] from sea to island. Return how many island are there in the matrix after each operator.You need to return an array of size K.

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.Example

**Example 1:**

```text
Input: n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]Output: [1,1,2,2]Explanation:0.  00000    00000    00000    000001.  00000    01000    00000    000002.  01000    01000    00000    000003.  01000    01000    00000    000104.  01000    01000    00000    00011
```

**Example 2:**

```text
Input: n = 3, m = 3, A = [[0,0],[0,1],[2,2],[2,1]]Output: [1,1,2,2]
```

## Solution - Union Find

If we use BFS here \(solution for 'Number of Islands'\), then the time complexity would be huge!

The max amount of operators can be \(n \* m\)

For every BFS operation can be O\(n \* m\), so the total time complexity can be O\(n^2 \* m ^2\), if n = m, then it would be O\(n^4\), too slow!

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

