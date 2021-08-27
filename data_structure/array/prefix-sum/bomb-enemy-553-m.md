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

## Solution - Brute Force Simulation

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

* **Time Complexity: O\(m \* n \* max\(m, n\)\)**
* **Space Complexity: O\(1\)**

## Solution - Prefix Sum

First calculate the prefix sum of each direction enemy's kill counts, then traverse the grid to sum the four direction enemy kills from the prefix sum 2D array

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
        if not grid:
            return 0
        
        # prefix sum of four diectional kills counts 
        left_right = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        right_left = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        top_down = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        down_top = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == GRID_TYPE.wall:
                    continue
                if col == 0:
                    left_right[row][col] = int(grid[row][col] == GRID_TYPE.enemy)
                else:
                    left_right[row][col] = left_right[row][col - 1] + int(grid[row][col] == GRID_TYPE.enemy)
        for row in range(len(grid)):
            for col in range(len(grid[0]) - 1, -1, -1):
                if grid[row][col] == GRID_TYPE.wall:
                    continue
                if col == len(grid[0]) - 1:
                    right_left[row][col] = int(grid[row][col] == GRID_TYPE.enemy)
                else:
                    right_left[row][col] = right_left[row][col + 1] + int(grid[row][col] == GRID_TYPE.enemy)
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col] == GRID_TYPE.wall:
                    continue
                if row==0:
                    top_down[row][col] = int(grid[row][col] == GRID_TYPE.enemy)
                else:
                    top_down[row][col] = top_down[row-1][col] + int(grid[row][col] == GRID_TYPE.enemy)
        
        for col in range(len(grid[0])):
            for row in range(len(grid)-1,-1,-1):
                if grid[row][col] == GRID_TYPE.wall:
                    continue
                if row==len(grid)-1:
                    down_top[row][col] = int(grid[row][col] == GRID_TYPE.enemy)
                else:
                    down_top[row][col] = down_top[row + 1][col] + int(grid[row][col] == GRID_TYPE.enemy)
        res = float('-inf')
        # finally traverse the grid and sum the four directional kill counts, and pick the maximum answer
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == GRID_TYPE.empty:
                    res = max(res, left_right[row][col] + right_left[row][col] + top_down[row][col] + down_top[row][col])
        return 0 if res == float('-inf') else res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(m \* n\)**
  * Construct prefix sum: O\(m\* n\)
  * Traverse grid: O\(m \* n\)
* **Space Complexity:**

