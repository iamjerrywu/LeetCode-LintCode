# Minimum Path Sum 110 \(E\)

## Problem

iven a m \* nm∗n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

The robot can only move either down or right at any point in time.Example

**Example 1:**

Input:

```text
grid = [[1,3,1],[1,5,1],[4,2,1]]
```

Output:

```text
7
```

Explanation:

Path is: 1 -&gt; 3 -&gt; 1 -&gt; 1 -&gt; 1

**Example 2:**

Input:

```text
grid = [[1,3,2]]
```

Output:

```text
6
```

Explanation:

Path is: 1 -&gt; 3 -&gt; 2  


## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]

        # init state
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        # dp state 
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[m - 1][n - 1]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

