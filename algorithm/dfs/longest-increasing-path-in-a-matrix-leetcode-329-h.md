# Longest Increasing Path in a Matrix (LeetCode 329) (H)

## Problem

Given an `m x n` integers `matrix`, return _the length of the longest increasing path in_ `matrix`.

From each cell, you can either move in four directions: left, right, up, or down. You **may not** move **diagonally** or move **outside the boundary** (i.e., wrap-around is not allowed).

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg)

```
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg)

```
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
```

**Example 3:**

```
Input: matrix = [[1]]
Output: 1
```

&#x20;

**Constraints:**

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 200`
* `0 <= matrix[i][j] <= 231 - 1`

## Solution - DFS + Memoization

Do early pruning that matains another matrix recording length that ending with matrix\[i]\[j]

So when deciding next step, we should also check that if the record\[i]\[j] should < than current length

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class Solution:
    def __init__(self):
        self.max_length = 0
                                        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
         # here the records is the longest distance ended with (i, j)
        records = [[1] * len(matrix[0]) for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited = set()
                self.dfs(i, j, 1, matrix, records, visited)
        return self.max_length
    
    def dfs(self, x, y, length, matrix, records, visited):
        if length > self.max_length:
            self.max_length = length
        records[x][y] = max(records[x][y], length)
        prev_val = matrix[x][y]
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if self.is_valid(new_x, new_y, matrix, records, visited, prev_val, length + 1):
                visited.add((new_x, new_y))
                self.dfs(new_x, new_y, length + 1, matrix, records, visited)
                visited.remove((new_x, new_y))
    
    def is_valid(self, x, y, matrix, records, visited, prev_val, length):
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
            return (x, y) not in visited and matrix[x][y] > prev_val and records[x][y] < length
        return False
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**

****

## Solution - DFS + Better Memoization

The memoization here is recording the longest length that start from (i, j) position

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class Solution:
                                        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        records = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, self.dfs(i, j, matrix, records))
        return ans
    def dfs(self, x, y, matrix, records):
        if records[x][y] != 0:
            return records[x][y]
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if self.is_valid(new_x, new_y, matrix, records, matrix[x][y]):
                records[x][y] = max(records[x][y], self.dfs(new_x, new_y, matrix, records))
        records[x][y]+=1
        return records[x][y]
    
    def is_valid(self, x, y, matrix, records, prev_val):
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
            return matrix[x][y] > prev_val
        return False
```
{% endtab %}
{% endtabs %}

* **Time Complexity:  O(mn)**
  * O(V + E)
    * V: number of vertices = m \* n
    * E: number of edges 4 \* V = 4 \* m \* n
* **Space Complexity:**
