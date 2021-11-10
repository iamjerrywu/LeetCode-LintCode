# Rotting Oranges (LeetCode 994) (M)

## Problem



You are given an `m x n` `grid` where each cell can have one of three values:

* `0` representing an empty cell,
* `1` representing a fresh orange, or
* `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return _the minimum number of minutes that must elapse until no cell has a fresh orange_. If _this is impossible, return_ `-1`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:**

```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

**Example 3:**

```
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 10`
* `grid[i][j]` is `0`, `1`, or `2`.

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class GridType:
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2

DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        oranges = 0
        queue = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == GridType.ROTTEN:
                    queue.append((i, j))
                if grid[i][j] != GridType.EMPTY:
                    oranges+=1
        
        rottens = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                rottens+=1
                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy
                    if self.is_fresh(new_x, new_y, grid):
                        grid[new_x][new_y] = GridType.ROTTEN
                        queue.append((new_x, new_y))
            ans+=1
        if oranges > 0:
            return ans - 1 if oranges == rottens else -1
        else:
            return 0
        
    
    def is_fresh(self, x, y, grid):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return grid[x][y] == GridType.FRESH
        return False
```
{% endtab %}
{% endtabs %}

* **Time Complexity: **
* **Space Complexity:**
