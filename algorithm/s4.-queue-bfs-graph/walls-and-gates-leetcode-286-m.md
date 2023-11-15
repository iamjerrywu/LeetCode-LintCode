# Walls and Gates (LeetCode 286) (M)



## Problem



You are given an `m x n` grid `rooms` initialized with these three possible values.

* `-1` A wall or an obstacle.
* `0` A gate.
* `INF` Infinity means an empty room. We use the value `231 - 1 = 2147483647` to represent `INF` as you may assume that the distance to a gate is less than `2147483647`.

Fill each empty room with the distance to _its nearest gate_. If it is impossible to reach a gate, it should be filled with `INF`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/03/grid.jpg)

```
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```

**Example 2:**

```
Input: rooms = [[-1]]
Output: [[-1]]
```

**Example 3:**

```
Input: rooms = [[2147483647]]
Output: [[2147483647]]
```

**Example 4:**

```
Input: rooms = [[0]]
Output: [[0]]
```

&#x20;

**Constraints:**

* `m == rooms.length`
* `n == rooms[i].length`
* `1 <= m, n <= 250`
* `rooms[i][j]` is `-1`, `0`, or `231 - 1`.

## Solution - BFS gate 1-by-1 (little slower)

{% tabs %}
{% tab title="Python" %}
```python
class RoomType:
    empty = 2147483647
    wall = -1
    gate = 0
DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
import collections
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # find every gates
        gates = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == RoomType.gate:
                    gates.append((i, j))
        queue = collections.deque()
        for gate in gates:
            queue.append(gate)
            self.bfs(queue, rooms)
        return rooms
    
    def bfs(self, queue, rooms):
        steps = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # should not update here, since it won't help to reduce BFS search
                # rooms[x][y] = min(rooms[x][y], steps)
                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy
                    if self.is_valid(new_x, new_y, rooms, steps + 1):
                        queue.append((new_x, new_y))
                        # update here is good, prevent duplicate location putting to queue
                        rooms[new_x][new_y] = min(rooms[new_x][new_y], steps + 1)
                        
            steps+=1
    
    def is_valid(self, x, y, rooms, steps):
        if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]):
            return rooms[x][y] > steps 
        return False
                
                
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:  O(m \* n)**
* **Space Complexity: O(m \* n)**



## Solution - BFS (all gates at once)

{% tabs %}
{% tab title="Python" %}
```python
class RoomType:
    empty = 2147483647
    wall = -1
    gate = 0
DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
import collections
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # find every gates
        queue = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == RoomType.gate:
                    queue.append((i, j))
        self.bfs(queue, rooms)
        return rooms
    
    def bfs(self, queue, rooms):
        steps = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # update here won't help too much on early prunning
                # if rooms[x][y] == RoomType.empty:
                #     rooms[x][y] = steps
                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy
                    if self.is_valid(new_x, new_y, rooms):
                        # should update distance here, since here can only prevant duplicate BFS research 
                        # that putting smae location to queue
                        rooms[new_x][new_y] = steps + 1
                        queue.append((new_x, new_y))
            steps+=1
    
    def is_valid(self, x, y, rooms):
        if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]):
            return rooms[x][y] == RoomType.empty
        return False
                
                
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:  O(m \* n)**
* **Space Complexity: O( m \* n)**
