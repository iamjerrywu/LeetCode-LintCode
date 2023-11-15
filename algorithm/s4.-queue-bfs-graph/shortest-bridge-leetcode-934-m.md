# Shortest Bridge (LeetCode 934) (M)

## Problem

You are given an `n x n` binary matrix `grid` where `1` represents land and `0` represents water.

An **island** is a 4-directionally connected group of `1`'s not connected to any other `1`'s. There are **exactly two islands** in `grid`.

You may change `0`'s to `1`'s to connect the two islands to form **one island**.

Return _the smallest number of_ `0`_'s you must flip to connect the two islands_.

&#x20;

**Example 1:**

```
Input: grid = [[0,1],[1,0]]
Output: 1
```

**Example 2:**

```
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
```

**Example 3:**

```
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
```

&#x20;

**Constraints:**

* `n == grid.length == grid[i].length`
* `2 <= n <= 100`
* `grid[i][j]` is either `0` or `1`.
* There are exactly two islands in `grid`.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
import collections
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        first_island = []
        queue = collections.deque()
        
        # find first island
        find = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    find = True
                    queue.append((i, j))
                    grid[i][j] = -1
                    # bfs
                    while queue:
                        x, y = queue.popleft()
                        # print(x, y)
                        first_island.append((x, y))
                        # print(first_island)
                        for dx, dy in DIRECTIONS:
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                                grid[new_x][new_y] = -1
                                queue.append((new_x, new_y))
                if find:
                    break
            if find:
                break
                    
        ans = float('inf')
        queue.clear()
        steps = {}
        for x, y in first_island:
            queue.append((x, y))
            dist = 0
            # bfs
            while queue:
                for _ in range(len(queue)):
                    cur_x, cur_y = queue.popleft()
                    if grid[cur_x][cur_y] == 1:
                        ans = min(ans, dist - 1)
                        queue.clear()
                        break
                    for dx, dy in DIRECTIONS:
                        new_x = cur_x + dx
                        new_y = cur_y + dy
                        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != -1:
                            if (new_x, new_y) not in steps or steps[(new_x, new_y)] > dist + 1:
                                steps[(new_x, new_y)] = dist + 1
                                queue.append((new_x, new_y))
                dist+=1
        return ans
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

