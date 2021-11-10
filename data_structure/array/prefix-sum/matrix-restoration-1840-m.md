# Matrix Restoration 1840 (M)

## Problem

There is a matrix beforebefore with nn rows and mm columns. For each element in before before\[i]\[j]before\[i]\[j], we will use the following algorithm to convert it to after \[i] \[j]after\[i]\[j]. Given the afterafter matrix, please restore the original matrix beforebefore.

```
s = 0for i1: 0 -> i    for j1: 0 -> j        s = s + before[i1][j1]after[i][j] = s
```

1 \leq n,m \leq 1\\,0001≤n,m≤1000Example

**Example1**

```
Input:22[[1,3],[4,10]]Output: [[1,2],[3,4]]Explanation:before:1 23 4after:1 34 10
```

## Solution&#x20;

![](<../../../.gitbook/assets/Screen Shot 2021-06-21 at 4.00.55 PM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: the row of the matrix
    @param m: the column of the matrix
    @param after: the matrix
    @return: restore the matrix
    """
    def matrixRestoration(self, n, m, after):
        # write your code here
        # after[i][j] = after[i - 1][j] + after[i][j - 1] + before[i][j] - after[i - 1][j - 1]
        # before[i][j] = after[i][j] − after[i − 1][j] − after[i][j − 1] + after[i − 1][j − 1]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # after[i][j] − after[i − 1][j]
                if i > 0:
                    after[i][j] -= after[i - 1][j]
                # after[i][j] − after[i][j − 1]  
                if j > 0:
                    after[i][j] -= after[i][j - 1]
                # after[i][j] + after[i − 1][j − 1]
                if i > 0 and j > 0:
                    after[i][j]+=after[i - 1][j - 1]            
        return after
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n \* m)**
* **Space Complexity: O(1)**

## Solution&#x20;

Since in python arr\[-1] means the last value, therefore with tricks that add 0 in both row/column, we can directly refer the before arr from after arr, without worryng about the boundary condition.

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: the row of the matrix
    @param m: the column of the matrix
    @param after: the matrix
    @return: restore the matrix
    """
    def matrixRestoration(self, n, m, after):
        # write your code here
        after.append([0] * m)
        for row in after:
            row.append(0)
        # after[i][j] = after[i - 1][j] + after[i][j - 1] + before[i][j] - after[i - 1][j - 1]
        # before[i][j] = after[i][j] − after[i − 1][j] − after[i][j − 1] + after[i − 1][j − 1]
        before = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                before[i][j] = after[i][j] - after[i - 1][j] - after[i][j - 1] + after[i - 1][j - 1]
        return before
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n \* m)**
* **Space Complexity: O(n + m) **
