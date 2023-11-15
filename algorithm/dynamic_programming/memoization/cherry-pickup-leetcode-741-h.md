# Cherry Pickup (LeetCode 741) (H)

## Problem



ou are given an `n x n` `grid` representing a field of cherries, each cell is one of three possible integers.

* `0` means the cell is empty, so you can pass through,
* `1` means the cell contains a cherry that you can pick up and pass through, or
* `-1` means the cell contains a thorn that blocks your way.

Return _the maximum number of cherries you can collect by following the rules below_:

* Starting at the position `(0, 0)` and reaching `(n - 1, n - 1)` by moving right or down through valid path cells (cells with value `0` or `1`).
* After reaching `(n - 1, n - 1)`, returning to `(0, 0)` by moving left or up through valid path cells.
* When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell `0`.
* If there is no valid path between `(0, 0)` and `(n - 1, n - 1)`, then no cherries can be collected.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/14/grid.jpg)

<pre><code>Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
<strong>Output:
</strong> 5
<strong>Explanation:
</strong> The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
</code></pre>

**Example 2:**

<pre><code>Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
<strong>Output:
</strong> 0
</code></pre>

&#x20;

**Constraints:**

* `n == grid.length`
* `n == grid[i].length`
* `1 <= n <= 50`
* `grid[i][j]` is `-1`, `0`, or `1`.
* `grid[0][0] != -1`
* `grid[n - 1][n - 1] != -1`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid or grid[0] == 0:
            return 0
        # two people going from (0, 0) -> (n -1, n - 1)
        memo = defaultdict(int)
        ans = self.dfs(0, 0, 0, 0, grid, memo)
        if ans < 0:
            return 0
        return ans
    
    def dfs(self, x1, y1, x2, y2, grid, memo):
        if (x1, y1, x2, y2) in memo:
            return memo[(x1, y1, x2, y2)]
        cur_cherry = 0
        if not self.is_valid(x1, y1, x2, y2, grid):
            return float('-inf')
        if x1 == x2 and y1 == y2:
            cur_cherry+=grid[x1][y1]
        else:
            cur_cherry+=grid[x1][y1] + grid[x2][y2]
        if x1 == len(grid) - 1 and y1 == len(grid[0]) - 1:
            return cur_cherry
        else:
            future_cherry = -float('inf')
            for dx1, dy1, dx2, dy2 in DIRECTIONS:
                new_x1 = x1 + dx1
                new_y1 = y1 + dy1
                new_x2 = x2 + dx2
                new_y2 = y2 + dy2
                
                future_cherry = max(future_cherry, self.dfs(new_x1, new_y1, new_x2, new_y2, grid, memo))
        cur_cherry+=future_cherry
        memo[(x1, y1, x2, y2)] = cur_cherry
        return cur_cherry
    
    def is_valid(self, x1, y1, x2, y2, grid):
        if x1 < 0 or x1 >= len(grid) or x2 < 0 or x2 >= len(grid) or y1 < 0 or y1 >= len(grid[0]) or y2 < 0 or y2 >= len(grid[0]) or grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return False
        return True
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
