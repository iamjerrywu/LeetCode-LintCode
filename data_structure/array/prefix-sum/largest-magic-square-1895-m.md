# Largest Magic Square 1895 (M)

## Problem



A `k x k` **magic square** is a `k x k` grid filled with integers such that every row sum, every column sum, and both diagonal sums are **all equal**. The integers in the magic square **do not have to be distinct**. Every `1 x 1` grid is trivially a **magic square**.

Given an `m x n` integer `grid`, return _the **size** (i.e., the side length _`k`_) of the **largest magic square** that can be found within this grid_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/05/29/magicsquare-grid.jpg)

```
Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/05/29/magicsquare2-grid.jpg)

```
Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 50`
* `1 <= grid[i][j] <= 106`

## Solution - Prefix Sum

If using brute force, the time complexity would be:

* O(n^5)m (n \~= m)
  * Traverse square: O(n\*m)
  * Find valid length: O(min(n, m))
  * Verify whether magic: O(min(n, m) ^2)
    * For rows, columns would need O(min(n, m) ^2)
    * For diagnose line, only need O(min(n, m))

If we apply using prefix sum, it can be reduced to O(n^4)

* O(n^4), (n \~= m)
  * Traverse square: O(n\*m)
  * Find valid length: O(min(n, m))
  * Verify whether magic: O(min(n, m))
    * For rows, columns would need O((n, m))
    * For diagnose line, only need O(min(n, m))

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        row_prefix_sum = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row_prefix_sum[i][j + 1] = row_prefix_sum[i][j] + grid[i][j]
        
        col_prefix_sum = [[0] * (n) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                col_prefix_sum[i + 1][j] = col_prefix_sum[i][j] + grid[i][j]
                
        max_length = min(m, n)
        while max_length > 1: # O(n)
            for i in range(m - max_length + 1): #O(n)
                for j in range(n - max_length + 1): #O(n)
                    diff = row_prefix_sum[i][j + max_length] - row_prefix_sum[i][j]
                    same = True
                    for k in range(max_length): #O(n)
                        if diff != row_prefix_sum[i + k][j + max_length] - row_prefix_sum[i + k][j]:
                            same = False
                            break
                        if diff != col_prefix_sum[i + max_length][j + k] - col_prefix_sum[i][j + k]:
                            same = False
                            break
                    if same:
                        diag_sum1 = 0
                        diag_sum2 = 0
                        for k in range(max_length): # O(n)
                            diag_sum1+=grid[i + k][j + k]
                            diag_sum2+=grid[i + k][j + max_length - k - 1]
                        if diff == diag_sum1 == diag_sum2:
                            return max_length
            max_length-=1
        return 1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^4)**
* **Space Complexity: O(n^2)**
