# Zombie in Matrix 598 \(M\)

## Problem

Description

Give a two-dimensional grid, each grid has a value, 2 for wall, 1 for zombie, 0 for human \(numbers 0, 1, 2\).Zombies can turn the nearest people\(up/down/left/right\) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return `-1` if can not turn all people into zombies.Example

Example 1:

```text
Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output:
2
```

Example 2:

```text
Input:
[[0,0,0],
 [0,0,0],
 [0,0,1]]
Output:
4
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        # cannot write as 'if not grid:
        # since if grid = [[]], it won't be effective

        n = len(grid)
        if n == 0:
            return 0
        
        m = len(grid[0])
        if m == 0:
            return 0
        
        queue = collections.deque()
        # every grid[x][y] can be the start points
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i, j))
        
        DIRECTIONS = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        days = 0
        while queue:
            days+=1
            for _ in range(len(queue)):
                node = queue.popleft()
                for k in range(4):
                    x = node[0] + DIRECTIONS[k][0]
                    y = node[1] + DIRECTIONS[k][1]
                    if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == 0:
                        grid[x][y] = 1
                        queue.append((x, y))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    return -1
        # need to -1
        # since the last round, grid[x][y] already = 1, but put in the queue so would execute one more time (to let queue = 0)
        return days - 1   
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\*m\)**
* **Space Complexity: O\(x\)**

