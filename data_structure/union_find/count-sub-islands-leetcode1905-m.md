# Count Sub Islands \(LeetCode1905\) \(M\)

## Problem

## Solution - BFS

Similar to 'Number of Islands 433' problem, however need to additionally check whether grid1 island is sub-island of grid2. 

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

* **Time Complexity: O\(m \* n\)**
  * m: len\(grid\)
  * n: len\(grid\[0\]\)
* **Space Complexity: O\(min\(m, n\)**

