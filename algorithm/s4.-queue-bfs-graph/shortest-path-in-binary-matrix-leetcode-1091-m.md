# Shortest Path in Binary Matrix (LeetCode 1091) (M)

## Problem

****

Given an `n x n` binary matrix `grid`, return _the length of the shortest **clear path** in the matrix_. If there is no clear path, return `-1`.

A **clear path** in a binary matrix is a path from the **top-left** cell (i.e., `(0, 0)`) to the **bottom-right** cell (i.e., `(n - 1, n - 1)`) such that:

* All the visited cells of the path are `0`.
* All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).

The **length of a clear path** is the number of visited cells of this path.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/18/example1\_1.png)

```
Input: grid = [[0,1],[1,0]]
Output: 2
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/18/example2\_1.png)

```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```

**Example 3:**

```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```

&#x20;

**Constraints:**

* `n == grid.length`
* `n == grid[i].length`
* `1 <= n <= 100`
* `grid[i][j] is 0 or 1`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        
        queue = collections.deque([(0, 0)])
        grid[0][0] = 1
        steps = 1
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return steps

                for dx, dy in DIRECTIONS:
                    new_x = x + dx
                    new_y = y + dy
                    if self.is_valid(new_x, new_y, grid):
                        # add here, to let the searching be faster
                        grid[new_x][new_y] = 1
                        queue.append((new_x, new_y))
            steps+=1
        return -1
    
    def is_valid(self, x, y, grid):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return grid[x][y] == 0
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

* **Time Complexity: O(n)**
  * n: number of cells
* **Space Complexity:**

****
