# Number of Distinct Islands 860 \(M\)

## Problem

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s \(representing land\) connected **4-directionally** \(horizontal or vertical.\) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated \(and not rotated or reflected\) to equal the other.

Return _the number of **distinct** islands_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/05/01/distinctisland1-1-grid.jpg)

```text
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/05/01/distinctisland1-2-grid.jpg)

```text
Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 50`
* `grid[i][j]` is either `0` or `1`.

## Solution - Brute Force DFS

Find the possible island's coordination list, then sort them and transform them into new coordination list \(the left upper coordination now align to origin\). Then turn these new coordination list to sets and find the len\(sets\), then that's the distinct islands numbers

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
import collections
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = collections.deque()
        islands = collections.defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    queue.append((i, j))
                    visited.add((i, j))
                    area, coord = self.search_islands(queue, grid, visited)
                    new_coord = self.process(coord)
                    if area not in islands:
                        islands[area] = set([(new_coord)])
                    else:
                        islands[area].add(new_coord)
        ans = 0
        for k, v_set in islands.items():
            ans+= len(v_set)
        return ans
    
    def search_islands(self, queue, grid, visited):
        area = 0
        coord = []
        while queue:
            x, y = queue.popleft()
            coord.append((x, y))
            area+=1
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if self.is_valid(new_x, new_y, visited, grid):
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
        return area, coord
    
    def is_valid(self, x, y, visited, grid):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
            return (x, y) not in visited
        return False
    
    def process(self, coord):
        coord.sort()
        new_coord = []
        diff_x, diff_y = coord[0][0], coord[0][1]
        for x, y in coord:
            new_coord.append((x - diff_x, y - diff_y))
        return tuple(new_coord)
        
```
{% endtab %}
{% endtabs %}

* **Time Complexity:** 
* **Space Complexity:** 

