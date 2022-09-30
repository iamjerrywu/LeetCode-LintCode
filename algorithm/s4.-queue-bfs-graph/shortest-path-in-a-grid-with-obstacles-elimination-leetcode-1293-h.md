# Shortest Path in a Grid with Obstacles Elimination (LeetCode 1293) (H)

## Problem

****

You are given an `m x n` integer matrix `grid` where each cell is either `0` (empty) or `1` (obstacle). You can move up, down, left, or right from and to an empty cell in **one step**.

Return _the minimum number of **steps** to walk from the upper left corner_ `(0, 0)` _to the lower right corner_ `(m - 1, n - 1)` _given that you can eliminate **at most** _ `k` _obstacles_. If it is not possible to find such walk return `-1`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/09/30/short1-grid.jpg)

<pre><code>Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
<strong>Output:
</strong> 6
<strong>Explanation:
</strong> 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/09/30/short2-grid.jpg)

<pre><code>Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
<strong>Output:
</strong> -1
<strong>Explanation:
</strong> We need to eliminate at least two obstacles to find such a walk.</code></pre>

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 40`
* `1 <= k <= m * n`
* `grid[i][j]` is either `0` **or** `1`.
* `grid[0][0] == grid[m - 1][n - 1] == 0`



## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque
DIRECTIONS = [[0, 1], [1, 0], [0, -1], [0, 1]]
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque([(0, 0, k)])
        steps = 0
        visited = set()
        while queue:
            for _ in range(len(queue)):
                x, y, k = queue.popleft()
                visited.add((x, y, k))
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return steps
                for dx, dy in DIRECTIONS:
                    new_x = x + dx
                    new_y = y + dy
                    if self.is_valid(new_x, new_y, k, visited, grid):
                        if k > 0 and grid[new_x][new_y] == 1 and (new_x, new_y, k) not in visited:
                            visited.add((x, y, k - 1))
                            queue.append((new_x, new_y, k - 1))
                        if grid[new_x][new_y] == 0 and (new_x, new_y, k) not in visited:    
                            visited.add((x, y, k))
                            queue.append((new_x, new_y, k))
            steps+=1
        return -1
        
    def is_valid(self, x, y, k, visited, grid):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return (x, y, k) not in visited
        return False

```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
