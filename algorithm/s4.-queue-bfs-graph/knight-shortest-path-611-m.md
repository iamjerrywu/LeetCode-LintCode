# Knight Shortest Path 611 \(M\)

## Problem

Given a knight in a chessboard \(a binary matrix with `0` as empty and `1` as barrier\) with a `source` position, find the shortest path to a `destination` position, return the length of the route.  
Return `-1` if destination cannot be reached.

source and destination must be empty.  
Knight can not enter the barrier.  
Path length refers to the number of steps the knight takes.Have you met this question in a real interview?  YesProblem Correction

#### Clarification

If the knight is at \(_x_, _y_\), he can get to the following positions in one step:

```text
(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
```

#### Example

**Example 1:**

```text
Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]
```

**Example 2:**

```text
Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output:-1
```

## Solution - BFS

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

from collections import deque

DIRECTIONS = (
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
)

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}
        
        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append((next_x, next_y))
        return -1
    
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return not grid[x][y]

        
        

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - Double Direction BFS

### Code

{% tabs %}
{% tab title="python" %}
```python
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

from collections import deque

DIRECTIONS = (
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
)

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or not grid[0]:
            return -1
        if grid[destination.x][destination.y]:
            return -1
        if (source.x, source.y) == (destination.x, destination.y):
            return 0
        
        forward_queue = deque([(source.x, source.y)])
        forward_set = set([(source.x, source.y)])
        backward_queue = deque([(destination.x, destination.y)])
        backward_set = set([(destination.x, destination.y)])

        distance = 0
        while forward_queue and backward_queue:
            distance+=1
            if self.extend_queue(grid, forward_queue, forward_set, backward_set):
                return distance
            distance+=1
            if self.extend_queue(grid, backward_queue, backward_set, forward_set):
                return distance
        return -1
    
    def extend_queue(self, grid, queue, visited, opposite_visited):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if not self.is_valid(grid, visited, new_x, new_y):
                    continue
                if (new_x, new_y) in opposite_visited:
                    return True
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
        return False
    
    def is_valid(self, grid, visited, x, y):
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y]:
            return False
        if (x, y) in visited:
            return False
        return True
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

