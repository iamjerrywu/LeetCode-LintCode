# Max Area of Island (1080) (E)

## Problem

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return _the maximum **area** of an island in_ `grid`. If there is no island, return `0`.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

**Example 2:**

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 50`
* `grid[i][j]` is either `0` or `1`.

## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1,0], [-1, 0], [0, 1], [0, -1]]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        ans = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    queue.append((i, j))
                    visited.add((i, j))
                    ans = max(ans, self.bfs(queue, grid, visited))
        return ans
    
    def bfs(self, queue, grid, visited):
        area = 0
        while queue:
            x, y = queue.pop()
            area+=1
            for dx, dy in DIRECTIONS:
                new_x = x + dx
                new_y = y + dy
                if self.is_valid(new_x, new_y, grid, visited):
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
        return area
    
    def is_valid(self, x, y, grid, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return grid[x][y] == 1 and (x, y) not in visited
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - BFS without visited

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
import collections
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        queue = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    queue.append((i, j))
                    ans = max(ans, self.bfs(queue, grid))
        return ans
    
    def bfs(self, queue, grid):
        area = 0
        while queue:
            x, y = queue.popleft()
            area+=1
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if self.is_valid(new_x, new_y, grid):
                    grid[new_x][new_y] = -1
                    queue.append((new_x, new_y))
        return area
    
        
    
    def is_valid(self, x, y, grid):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return grid[x][y] == 1
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - DFS

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1,0], [-1, 0], [0, 1], [0, -1]]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        ans = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    ans = max(ans, self.dfs(i, j, 1, grid, visited))
        return ans
    
    def dfs(self, x, y, area, grid, visited):
        for dx, dy in DIRECTIONS:
            new_x = x + dx
            new_y = y + dy
            if self.is_valid(new_x, new_y, grid, visited):
                visited.add((new_x, new_y))
                area = self.dfs(new_x, new_y, area + 1, grid, visited)
        return area
    
    def is_valid(self, x, y, grid, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return grid[x][y] == 1 and (x, y) not in visited
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - DFS without visited

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    ans = max(ans, self.dfs(i, j, grid))
        return ans
    
    def dfs(self, x, y, grid):
        area = 1
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if self.is_valid(new_x, new_y, grid):
                grid[new_x][new_y] = -1
                area+=self.dfs(new_x, new_y, grid)
        return area
    
    def is_valid(self, x, y, grid):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return grid[x][y] == 1
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - Union Find

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
