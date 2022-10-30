# Making a Large Island (LeetCOde 827) (H)

## Problem

****

You are given an `n x n` binary matrix `grid`. You are allowed to change **at most one** `0` to be `1`.

Return _the size of the largest **island** in_ `grid` _after applying this operation_.

An **island** is a 4-directionally connected group of `1`s.

&#x20;

**Example 1:**

<pre><code>Input: grid = [[1,0],[0,1]]
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> Change one 0 to 1 and connect two 1s, then we get an island with area = 3.</code></pre>

**Example 2:**

<pre><code>Input: grid = [[1,1],[1,0]]
<strong>Output:
</strong> 4
<strong>Explanation: 
</strong>Change the 0 to 1 and make the island bigger, only one island with area = 4.</code></pre>

**Example 3:**

<pre><code>Input: grid = [[1,1],[1,1]]
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> Can't change any 0 to 1, only one island with area = 4.</code></pre>

&#x20;

**Constraints:**

* `n == grid.length`
* `n == grid[i].length`
* `1 <= n <= 500`
* `grid[i][j]` is either `0` or `1`.



## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        island_idx = 2
        mapping = defaultdict(int)
        queue = deque()
        ans = 0
        # first traverse, find the island area and mark all that grid[x][y] as island_idx val
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] == island_idx
                    queue.append((i, j))
                    area = self.bfs(queue, grid, island_idx)
                    # need to record the area as ans here, since might be ans that no water in grid
                    ans = max(ans, area)
                    mapping[island_idx] = area
                    island_idx+=1
        
        # traverse second time based on water spot
        # check on the neighbors, if it's island, add up the mapping area
        # make sure that those neighbors belong to same island, shouldn't be added again
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    max_area = self.check_neighbors(i, j, grid, mapping)
                    ans = max(ans, max_area)
        return ans
    
    def bfs(self, queue, grid, island_idx):
        cnt = 0
        while queue:
            x, y = queue.popleft()
            cnt+=1
            grid[x][y] = island_idx
            for dx, dy in DIRECTIONS:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = island_idx
                    queue.append((new_x, new_y))
        return cnt
    
    def check_neighbors(self, x, y, grid, mapping):
        seen = set()
        area = 1
        for dx, dy in DIRECTIONS:
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                island_idx = grid[new_x][new_y]
                if island_idx not in seen:
                    area+=mapping[island_idx]
                    seen.add(island_idx)
        return area - BFS
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
