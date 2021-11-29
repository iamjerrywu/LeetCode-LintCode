# Shortest Distance from All Buildings (LeetCode 317) (H)

## Problem

&#x20;

You are given an `m x n` grid `grid` of values `0`, `1`, or `2`, where:

* each `0` marks **an empty land** that you can pass by freely,
* each `1` marks **a building** that you cannot pass through, and
* each `2` marks **an obstacle** that you cannot pass through.

You want to build a house on an empty land that reaches all buildings in the **shortest total travel** distance. You can only move up, down, left, and right.

Return _the **shortest travel distance** for such a house_. If it is not possible to build such a house according to the above rules, return `-1`.

The **total travel distance** is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using [Manhattan Distance](http://en.wikipedia.org/wiki/Taxicab\_geometry), where `distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/buildings-grid.jpg)

```
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
```

**Example 2:**

```
Input: grid = [[1,0]]
Output: 1
```

**Example 3:**

```
Input: grid = [[1]]
Output: -1
```

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 50`
* `grid[i][j]` is either `0`, `1`, or `2`.
* There will be **at least one** building in the `grid`.

## Solution - BFS (LTE)

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return -1
        total_buildings = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    total_buildings+=1
        # from that point, you can reach how many buildings
        reach = [[0] * m for _ in range(n)]
        # the total distance that you required to reach all the buildings
        dist = [[0] * m for _ in range(n)]
        
        queue = collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    self.bfs(queue, grid, reach, dist)
                    
        min_dist = float('inf')
        for i in range(n):
            for j in range(m):
                if reach[i][j] == total_buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        
        return min_dist if min_dist != float('inf') else -1
    
    def bfs(self, queue, grid, reach, dist):
        visited = set()
        visited.add((queue[-1][0], queue[-1][1]))
        distance = 0
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy
                    if self.is_valid(new_x, new_y, grid, visited):
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
                        reach[new_x][new_y]+=1
                        dist[new_x][new_y]+=distance + 1
            distance+=1
    
    def is_valid(self, x, y, grid, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return (x, y) not in visited and grid[x][y] == 0
        return False
                
                
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**

## Solution - BFS (Prunning)

When doing BFS (start from one single building), here can make sure if from that building, we cannot reach all the other buildings, then do early return -1 &#x20;

The reason behind this is that we can only find the shortest path to all the building if those buliding are reachable from either building.&#x20;

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return -1
        total_buildings = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    total_buildings+=1
        # from that point, you can reach how many buildings
        reach = [[0] * m for _ in range(n)]
        # the total distance that you required to reach all the buildings
        dist = [[0] * m for _ in range(n)]
        
        queue = collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    if not self.bfs(queue, grid, reach, dist, total_buildings):
                        return -1
                    
        min_dist = float('inf')
        for i in range(n):
            for j in range(m):
                if reach[i][j] == total_buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        
        return min_dist if min_dist != float('inf') else -1
    
    def bfs(self, queue, grid, reach, dist, total_buildings):
        building_cnt = 1
        
        visited = set()
        visited.add((queue[-1][0], queue[-1][1]))
        distance = 0
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy
                    if self.is_building(new_x, new_y, grid, visited):
                        building_cnt+=1
                        visited.add((new_x, new_y))
                    if self.is_valid(new_x, new_y, grid, visited):
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
                        reach[new_x][new_y]+=1
                        dist[new_x][new_y]+=distance + 1
            distance+=1
        return building_cnt == total_buildings
    
    def is_valid(self, x, y, grid, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return (x, y) not in visited and grid[x][y] == 0
        return False
    def is_building(self, x, y, grid, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return grid[x][y] == 1 and (x, y) not in visited
        return False
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
