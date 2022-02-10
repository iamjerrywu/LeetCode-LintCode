# Pacific Atlantic Water Flow (LeetCode 417) (M)

## Problem

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return _a **2D list** of grid coordinates_ `result` _where_ `result[i] = [ri, ci]` _denotes that rain water can flow from cell_ `(ri, ci)` _to **both** the Pacific and Atlantic oceans_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)

```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Example 2:**

```
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
```

&#x20;

**Constraints:**

* `m == heights.length`
* `n == heights[r].length`
* `1 <= m, n <= 200`
* `0 <= heights[r][c] <= 105`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
import collections
DIRECTIONS = [[1, 0], [-1, 0], [0, -1], [0, 1]]
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        achieved = set()
        visited = set()
        ans = []
        queue = collections.deque()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                # print(achieved)
                queue.append((i, j))
                visited.add((i, j))
                self.bfs(queue, heights, achieved, visited)
                visited.clear()
                queue.clear()
        return achieved
    
    def bfs(self, queue, heights, achieved, visited):
        reach_P = False
        reach_A = False
        ori_x, ori_y = queue[-1][0], queue[-1][1]
        while queue:
            x, y = queue.popleft()
            if (x, y) in achieved:
                achieved.add((ori_x, ori_y))
                return True
            if x == 0 or y == 0:
                reach_P = True
            if x == len(heights) - 1 or y == len(heights[0]) - 1:
                reach_A = True
            if reach_P and reach_A:
                
                achieved.add((ori_x, ori_y))
                return
            val = heights[x][y]
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if self.is_valid(new_x, new_y, val, heights, visited):
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        return
    
    def is_valid(self, x, y, val, heights, visited):
        if 0 <= x < len(heights) and 0 <= y < len(heights[0]):
            return (x, y) not in visited and heights[x][y] <= val
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

* **Time Complexity:**
* **Space Complexity:**

****
