# Number of Islands 433 \(E\)

## Problem

Given a boolean 2D matrix, `0` is represented as the sea, `1` is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.Have you met this question in a real interview?  YesProblem Correction

#### Example

**Example 1:**

```text
Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3
```

**Example 2:**

```text
Input:
[
  [1,1]
]
Output:
1
```

## Solution - BFS

### Code

{% tabs %}
{% tab title="python" %}
```python
from collections import deque

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        visited = set()
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    ans+=1
                    self.bfs(grid, visited, i, j)
        return ans
    
    def bfs(self, grid, visited, sx, sy):

        queue = deque([(sx, sy)])
        # already visited
        visited.add((sx, sy))
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                next_x = x + dx
                next_y = y + dy
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
    
    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m) or (x, y) in visited:
            return False
        return grid[x][y]
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - DFS

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    # dfs solution
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        
        islands = 0
        for row in range(n):
            for col in range(m):
                if self.is_island(grid, row, col, visited):
                    visited[row][col] = True
                    self.dfs(grid, row, col, visited)
                    islands+=1
        return islands

    def is_island(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if (x < 0 or x >= n) or (y < 0 or y >= m):
            return False
        if not grid[x][y]:
            return False
        return not visited[x][y]
    
    def dfs(self, grid, x, y, visited):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for (dx, dy) in DIRECTIONS:
            new_x = x + dx
            new_y = y + dy
            
            if self.is_island(grid, new_x, new_y, visited):
                visited[new_x][new_y] = True
                self.dfs(grid, new_x, new_y, visited)
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - Union Find

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

