# Number of Islands 433 (E)

## Problem

Given a boolean 2D matrix, `0` is represented as the sea, `1` is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.Have you met this question in a real interview?  YesProblem Correction

#### Example

**Example 1:**

```
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

```
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
```cpp
```
{% endtab %}

{% tab title="Untitled" %}
```cpp

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        queue<pair<int, int>> queue;
        int ans = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    grid[i][j] = '0';
                    queue.push(pair(i, j));
                    bfs(queue, grid);
                    ans+=1;
                }
            }
        }
        return ans;
    }
    
    void bfs (queue<pair<int, int>> &queue, vector<vector<char>> &grid) {
        vector<int> dx = {0, 1, 0, -1};
        vector<int> dy = {1, 0, -1, 0};
        
        while (!queue.empty()) {
            pair<int, int> pos = queue.front();
            queue.pop();
            for (int i = 0; i < dx.size(); i++) {
                int new_x = pos.first + dx[i];
                int new_y = pos.second + dy[i];
                
                if (isValid(new_x, new_y, grid)) {
                    grid[new_x][new_y] = '0';
                    queue.push(pair(new_x, new_y));
                }
            }
        }
    }
    
    bool isValid(int new_x, int new_y, vector<vector<char>> &grid) {
        if ((new_x >= 0) && (new_x < grid.size()) && (new_y >= 0) && (new_y < grid[0].size())) {
            return grid[new_x][new_y] == '1';
        }
        return false;
    }
};
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

{% tab title="c++" %}
```cpp

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int ans = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    grid[i][j] = '0';
                    dfs(i, j, grid);
                    ans+=1;
                }
            }
        }
        return ans;
    }
    
    void dfs (int x, int y, vector<vector<char>> &grid) {
        vector<int> dx = {0, 1, 0, -1};
        vector<int> dy = {1, 0, -1, 0};
        
        
        for (int i = 0; i < dx.size(); i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];

            if (isValid(new_x, new_y, grid)) {
                grid[new_x][new_y] = '0';
                dfs(new_x, new_y, grid);
            }
        }
    }
    
    bool isValid(int new_x, int new_y, vector<vector<char>> &grid) {
        if ((new_x >= 0) && (new_x < grid.size()) && (new_y >= 0) && (new_y < grid[0].size())) {
            return grid[new_x][new_y] == '1';
        }
        return false;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(m \* n)**
  * m: len(grid)
  * n: len(grid\[0])
* **Space Complexity: O(m \* n)**
  * Max recursion depth O(m \* n)

## Solution - Union Find

### Code

{% tabs %}
{% tab title="python" %}
```python
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

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
        
        self.father = {}
        self.size = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.father[(i, j)] = (i, j)
                    self.size+=1
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    for delta_x, delta_y in DIRECTIONS:
                        new_x = x + delta_x
                        new_y = y + delta_y
                        if self.is_valid(grid, new_x, new_y):
                            self.union((x, y), (new_x, new_y))
        return self.size

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.father[root_a] = root_b
            self.size-=1

    def find(self, point):
        root = point
        while root != self.father[root]:
            root = self.father[root]
        
        while point != root:
            original_father = self.father[point]
            self.father[point] = root
            point = original_father
        return root
    
    def is_valid(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        return grid[x][y]

        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
