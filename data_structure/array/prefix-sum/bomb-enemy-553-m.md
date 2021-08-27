# Bomb Enemy 553 \(M\)

## Problem

Given an `m x n` matrix `grid` where each cell is either a wall `'W'`, an enemy `'E'` or empty `'0'`, return _the maximum enemies you can kill using one bomb_. You can only place the bomb in an empty cell.

The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/03/27/bomb1-grid.jpg)

```text
Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/03/27/bomb2-grid.jpg)

```text
Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
Output: 1
```

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 500`
* `grid[i][j]` is either `'W'`, `'E'`, or `'0'`.

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class GRID_TYPE:
    wall = 'W'
    enemy = 'E'
    empty = '0'

class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == GRID_TYPE.empty:
                    ans = max(ans, self.find_kills(i, j, grid))
        return ans
    
    def find_kills(self, x, y, grid):
        cnt = 0
        cal_x = x
        while cal_x >=0 and grid[cal_x][y] != GRID_TYPE.wall:
            if grid[cal_x][y] == GRID_TYPE.enemy:
                cnt+=1
            cal_x-=1
        cal_x = x
        while cal_x < len(grid) and grid[cal_x][y] != GRID_TYPE.wall:
            if grid[cal_x][y] == GRID_TYPE.enemy:
                cnt+=1
            cal_x+=1
        cal_y = y
        while cal_y >=0 and grid[x][cal_y] != GRID_TYPE.wall:
            if grid[x][cal_y] == GRID_TYPE.enemy:
                cnt+=1
            cal_y-=1
        cal_y = y
        while cal_y < len(grid[0]) and grid[x][cal_y] != GRID_TYPE.wall:
            if grid[x][cal_y] == GRID_TYPE.enemy:
                cnt+=1
            cal_y+=1
        return cnt
            
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

