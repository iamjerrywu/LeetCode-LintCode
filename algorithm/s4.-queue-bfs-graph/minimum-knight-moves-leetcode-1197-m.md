# Minimum Knight Moves (LeetCode 1197) (M)

## Problem

n an **infinite** chess board with coordinates from `-infinity` to `+infinity`, you have a **knight** at square `[0, 0]`.

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

![](https://assets.leetcode.com/uploads/2018/10/12/knight.png)

Return _the minimum number of steps needed to move the knight to the square_ `[x, y]`. It is guaranteed the answer exists.

&#x20;

**Example 1:**

```
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
```

**Example 2:**

```
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
```

&#x20;

**Constraints:**

* `-300 <= x, y <= 300`
* `0 <= |x| + |y| <= 300`

## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
import collections
class Solution: 
    def minKnightMoves(self, x: int, y: int) -> int:
        steps = 0
        visited = set([(0, 0)])
        
        return self.dfs(0, 0, x, y, visited, steps)
    
    def dfs(self, i, j, x, y, visited, steps):
        print(i, j)
        if i == x and j == y:
            return steps
        for di, dj in DIRECTIONS:
            new_i, new_j = i + di, j + dj
            if self.is_valid(new_i, new_j, visited):
                visited.add((new_i, new_j))
                self.dfs(new_i, new_j, x, y, visited, steps + 1)
                visited.remove((new_i, new_j))
                
    def is_valid(self, x, y, visited):
        return (x, y) not in visited
        
    
```
{% endtab %}
{% endtabs %}

* **Time Complexity: **
* **Space Complexity:**
