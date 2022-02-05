# Detect Cycles in 2D Grid (LeetCode 1559) (M)

## Problem

****

Given a 2D array of characters `grid` of size `m x n`, you need to find if there exists any cycle consisting of the **same value** in `grid`.

A cycle is a path of **length 4 or more** in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the **same value** of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle `(1, 1) -> (1, 2) -> (1, 1)` is invalid because from `(1, 2)` we visited `(1, 1)` which was the last visited cell.

Return `true` if any cycle of the same value exists in `grid`, otherwise, return `false`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/07/15/1.png)

```
Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/07/15/22.png)

```
Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/07/15/3.png)

```
Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false
```

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 500`
* `grid` consists only of lowercase English letters.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
    
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    prev_x, prev_y = -1, -1
                    if self.dfs(i, j, grid, prev_x, prev_y, visited):
                        return True
        return False
    
    
    def dfs(self, x, y, grid, prev_x, prev_y, visited):
        if (x, y) in visited:
            return True
        
        visited.add((x, y))
        for dx, dy in DIRECTIONS:
            new_x = x + dx
            new_y = y + dy
            cur_val = grid[x][y]
            if self.is_valid(new_x, new_y, grid, cur_val, prev_x, prev_y):
                if self.dfs(new_x, new_y, grid, x, y, visited):
                    return True
        return False
    
    def is_valid(self, x, y, grid, cur_val, prev_x, prev_y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return grid[x][y] == cur_val and (x != prev_x or y != prev_y)
        return False
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

* **Time Complexity: O(n \* m)**
* **Space Complexity:**

****
