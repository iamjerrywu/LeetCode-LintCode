# Build Post Office II 573 \(H\)

## Problem

Given a 2D grid, each cell is either a wall `2`, an house `1` or empty `0` \(the number zero, one, two\), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.

Returns the sum of the minimum distances from all houses to the post office.Return `-1` if it is not possible.

* You cannot pass through wall and house, but can pass through empty.
* You only build post office on an empty.

Example

**Example 1:**

```text
Input：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]Output：8Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
```

**Example 2:**

```text
Input：[[0,1,0],[1,0,1],[0,1,0]]Output：4Explanation： Placing a post office at (1,1), th
```

## Solution - BFS

Start from every empty space in grid, and calculate whether it can reach every house or not, meanwhile maintain the min\_dist sum

### Code

{% tabs %}
{% tab title="python" %}
```python
class GridType:
    EMPTY = 0
    HOUSE = 1
    WALL = 2

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        min_dist = float('inf')
        
        # traverse every empty point (as start point)
        # then calculate the distance dict (containing each point it can reach, and the distance)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == GridType.EMPTY:
                    distance = self.bfs(grid, i, j)
                    min_dist = min(min_dist, self.get_distance_sum(distance, grid))
        
        return min_dist if min_dist != float('inf') else -1
    
    def bfs(self, grid, i, j):
        distance = {(i, j) : 0}
        queue = collections.deque([(i, j)])

        while queue:
            x, y = queue.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                adj_x, adj_y = x + dx, y + dy
                if not self.is_valid(adj_x, adj_y, grid):
                    continue
                if (adj_x, adj_y) in distance:
                    continue
                # distance: the location (x', y') with distance that can be reach from point (x, y)
                distance[(adj_x, adj_y)] = distance[(x, y)] + 1
                if grid[adj_x][adj_y] != GridType.HOUSE:
                    queue.append((adj_x, adj_y))
        return distance
    
    def get_distance_sum(self, distance, grid):
        distance_sum = 0
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val == GridType.HOUSE:
                    if (x, y) not in distance:
                        return float('inf')
                    distance_sum += distance[(x, y)]
        return distance_sum
    
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return grid[x][y] in [GridType.EMPTY, GridType.HOUSE] 
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - BFS \(2\)

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

\*\*\*\*

