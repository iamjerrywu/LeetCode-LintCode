# Build Post Office II 573 (H)

## Problem

Given a 2D grid, each cell is either a wall `2`, an house `1` or empty `0` (the number zero, one, two), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.

Returns the sum of the minimum distances from all houses to the post office.Return `-1` if it is not possible.

* You cannot pass through wall and house, but can pass through empty.
* You only build post office on an empty.

Example

**Example 1:**

```
Input：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]Output：8Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
```

**Example 2:**

```
Input：[[0,1,0],[1,0,1],[0,1,0]]Output：4Explanation： Placing a post office at (1,1), th
```

## Solution - BFS

#### Enumerate Post Office Location

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

* **Time Complexity: O(space \* n \* m)**
  * Space: the empty space amounts
  * n: len(grid), m: len(grid\[0])
  * Calculate all point's distance to post office: O(n\*m)
  * Worst case: O(n^2 \* m^2)
* **Space Complexity:**&#x20;



## Solution - BFS (2)

#### Enumerate House Location

Start from each houese, and from that house, do BFS to find out every empty place that it can reach (for those it can reach, record how many it can be reached from houses, and the distance). Eventually just calculate to have the min\_dist sum to have the answer.

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
        distance_sum = {}
        reachable_cnt = {}
        houses = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == GridType.HOUSE:
                    self.bfs(grid, i, j, distance_sum, reachable_cnt)
                    houses+=1
        
        min_dist = float('inf')
        for i in range(n):
            for j in range(m):
                if (i, j) not in reachable_cnt:
                    continue
                if reachable_cnt[(i, j)] != houses:
                    continue
                min_dist = min(min_dist, distance_sum[(i, j)])
            
        return min_dist if min_dist != float('inf') else -1
    
    def bfs(self, grid, i, j, distance_sum, reachable_cnt):
        distance = {(i, j) : 0}
        queue = collections.deque([(i, j)])

        while queue:
            x, y = queue.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                adj_x, adj_y = x + dx, y + dy
                if not self.is_valid(adj_x, adj_y, grid):
                    continue
                if (adj_x, adj_y) not in distance:
                    queue.append((adj_x, adj_y))
                    distance[(adj_x, adj_y)] = distance[(x, y)] + 1

                    # add up into distance_sum & reachable_cnt
                    if (adj_x, adj_y) not in reachable_cnt:
                        distance_sum[(adj_x, adj_y)] = 0
                        reachable_cnt[(adj_x, adj_y)] = 0
                    distance_sum[(adj_x, adj_y)] += distance[(adj_x, adj_y)]
                    reachable_cnt[(adj_x, adj_y)] +=1
    
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return grid[x][y] == GridType.EMPTY
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(House \* n \* m)**
  * HOuse: the empty House amounts
  * n: len(grid), m: len(grid\[0])
  * Calculate all point's distance to post office: O(n\*m)
  * Worst case: O(n^2 \* m^2)
* **Space Complexity:**&#x20;

