# Maximal Square 436 \(M\)

## Problem

Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, _find the largest square containing only_ `1`'s _and return its area_.

**Example 1:**![](https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg)

```text
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
```

**Example 2:**![](https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg)

```text
Input: matrix = [["0","1"],["1","0"]]
Output: 1
```

**Example 3:**

```text
Input: matrix = [["0"]]
Output: 0
```

**Constraints:**

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 300`
* `matrix[i][j]` is `'0'` or `'1'`.



## Solution - Brute Force



{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, self.count_square(i, j, matrix))
        return ans 
    
    # starting from i, j, and begin search for the possible maximum square area
    def count_square(self, i, j, matrix):
        area = 0
        tmp_i = i
        tmp_j = j
        for length in range(1, min(len(matrix) - i, len(matrix[0]) - j) + 1):
            for x in range(i, i + length):
                if matrix[x][tmp_j] != '1':
                    return area

            for y in range(j, j + length):
                if matrix[tmp_i][y] != '1':
                    return area
            tmp_i+=1
            tmp_j+=1
            area = length * length
        return area
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:  O\(n \* m  \* \(n + m\)\)**
  * n: len\(matrix\)
  * m: len\(matrix\[0\]\)
* **Space Complexity: O\(1\)**

## Solution - DP

{% tabs %}
{% tab title="Python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:** 
* **Space Complexity:** 

