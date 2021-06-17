# Maximal Rectangle 510 \(H\)

## Problem

Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return _its area_.

**Example 1:**![](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)

```text
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
```

**Example 2:**

```text
Input: matrix = []
Output: 0
```

**Example 3:**

```text
Input: matrix = [["0"]]
Output: 0
```

**Example 4:**

```text
Input: matrix = [["1"]]
Output: 1
```

**Example 5:**

```text
Input: matrix = [["0","0"]]
Output: 0
```

**Constraints:**

* `rows == matrix.length`
* `cols == matrix[i].length`
* `0 <= row, cols <= 200`
* `matrix[i][j]` is `'0'` or `'1'`.

## Solution - Brute Force

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        max_matrix_area = 0
        for up in range(n):
            for down in range(up + 1, n + 1):
                for left in range(m):
                    for right in range(left + 1, m + 1):
                        if self.is_rectangle(matrix, up, down, left, right):
                            max_matrix_area = max(max_matrix_area, (down - up) * (right - left))
        return max_matrix_area
    
    def is_rectangle(self, matrix, up, down, left, right):
        for i in range(up, down):
            for j in range(left, right):
                if not matrix[i][j]:
                    return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

