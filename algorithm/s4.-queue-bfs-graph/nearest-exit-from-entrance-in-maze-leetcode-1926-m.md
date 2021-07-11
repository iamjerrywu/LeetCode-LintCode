# Nearest Exit from Entrance in Maze \(LeetCode 1926\) \(M\)

## Problem

You are given an `m x n` matrix `maze` \(**0-indexed**\) with empty cells \(represented as `'.'`\) and walls \(represented as `'+'`\). You are also given the `entrance` of the maze, where `entrance = [entrancerow, entrancecol]` denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell **up**, **down**, **left**, or **right**. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the **nearest exit** from the `entrance`. An **exit** is defined as an **empty cell** that is at the **border** of the `maze`. The `entrance` **does not count** as an exit.

Return _the **number of steps** in the shortest path from the_ `entrance` _to the nearest exit, or_ `-1` _if no such path exists_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/06/04/nearest1-grid.jpg)

```text
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/06/04/nearesr2-grid.jpg)

```text
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
```

**Example 3:**![](https://assets.leetcode.com/uploads/2021/06/04/nearest3-grid.jpg)

```text
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
```

## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [(1,0), (-1,0), (0,-1), (0, 1)]
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        start = (entrance[0], entrance[1], 0)
        queue = collections.deque([start])
        visited = set([(entrance[0], entrance[1])])
        while queue:
            x, y, steps = queue.popleft()
            for dx, dy in DIRECTIONS:
                new_x = x + dx
                new_y = y + dy
                if self.left_from_exit(steps, maze, new_x, new_y):
                    return steps
                if self.is_valid(maze, new_x, new_y, visited):
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, steps + 1))
        return -1
    
    def left_from_exit(self, steps, maze, x, y):
        m = len(maze)
        n = len(maze[0])
        # steps cannot be 0 since cannot exist from entrance
        if steps != 0 and (x < 0 or x >= m or y < 0 or y >= n):
            return True
        return False
    
    def is_valid(self, maze, x, y, visited):
        m = len(maze)
        n = len(maze[0])
        
        if 0 <= x < m and 0 <= y < n and maze[x][y] == '.':
            return (x, y) not in visited
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

