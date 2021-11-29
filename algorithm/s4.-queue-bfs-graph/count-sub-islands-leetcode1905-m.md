# Count Sub Islands (LeetCode1905) (M)

## Problem



You are given two `m x n` binary matrices `grid1` and `grid2` containing only `0`'s (representing water) and `1`'s (representing land). An **island** is a group of `1`'s connected **4-directionally** (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in `grid2` is considered a **sub-island** if there is an island in `grid1` that contains **all** the cells that make up **this** island in `grid2`.

Return the _**number** of islands in_ `grid2` _that are considered **sub-islands**_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/06/10/test1.png)

```
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/06/03/testcasex2.png)

```
Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
```

**Constraints:**

* `m == grid1.length == grid2.length`
* `n == grid1[i].length == grid2[i].length`
* `1 <= m, n <= 500`
* `grid1[i][j]` and `grid2[i][j]` are either `0` or `1`.

## Solution - BFS

Similar to 'Number of Islands 433' problem, however need to additionally check whether grid1 island is sub-island of grid2.&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
DIRECTIONS = ([1, 0], [-1, 0], [0, 1], [0, -1])
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid2 or not grid2[0]:
            return 0
        visited = set()
        queue = collections.deque()
        sub_islands = 0
        n, m = len(grid2), len(grid2[0])
        for i in range(n):
            for j in range(m): 
                is_subislands = True
                if grid2[i][j] != 1 or (i, j) in visited:
                    continue
                is_subislands = self.is_subisland(i, j, grid1)
                queue.append((i, j))
                visited.add((i, j))
                while queue:
                    (x, y) = queue.popleft()
                    for dx, dy in DIRECTIONS:
                        new_x = x + dx
                        new_y = y + dy
                        if self.is_island(new_x, new_y, visited, grid2):
                            if is_subislands:
                                is_subislands = self.is_subisland(new_x, new_y, grid1)
                            queue.append((new_x, new_y))
                            visited.add((new_x, new_y))
                if is_subislands:
                    sub_islands+=1
        return sub_islands
    
    def is_island(self, x, y, visited, grid2):
        if x < 0 or x >= len(grid2) or y < 0 or y >= len(grid2[0]):
            return False
        return (x, y) not in visited and grid2[x][y] == 1
    
    def is_subisland(self, x, y, grid1):
        return grid1[x][y] == 1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(m \* n)**
  * m: len(grid)
  * n: len(grid\[0])
* **Space Complexity: O(min(m, n)**

## Solution - DFS

### Code

{% tabs %}
{% tab title="python" %}
```python
DIRECTIONS = ([1, 0], [-1, 0], [0, 1], [0, -1])
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid2 or not grid2[0]:
            return 0
        visited = set()
        queue = collections.deque()
        sub_islands = 0
        n, m = len(grid2), len(grid2[0])
        for i in range(n):
            for j in range(m): 
                is_subislands = True
                if grid2[i][j] != 1 or (i, j) in visited:
                    continue
                is_subislands = self.is_subisland(i, j, grid1)
                queue.append((i, j))
                visited.add((i, j))
                if self.dfs(i, j, visited, is_subislands, grid1, grid2):
                    sub_islands+=1
        return sub_islands
    
    def dfs(self, x, y, visited, is_subislands, grid1, grid2):
        for dx, dy in DIRECTIONS:
            new_x = x + dx
            new_y = y + dy
            if self.is_island(new_x, new_y, visited, grid2):
                visited.add((new_x, new_y))
                if is_subislands:
                    is_subislands = self.is_subisland(new_x, new_y, grid1)
                is_subislands = self.dfs(new_x, new_y, visited, is_subislands, grid1, grid2)
        return is_subislands
    
    def is_island(self, x, y, visited, grid2):
        if x < 0 or x >= len(grid2) or y < 0 or y >= len(grid2[0]):
            return False
        return (x, y) not in visited and grid2[x][y] == 1
    
    def is_subisland(self, x, y, grid1):
        return grid1[x][y] == 1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
