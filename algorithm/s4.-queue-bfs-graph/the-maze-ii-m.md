# The Maze II 788 \(M\)

## Problem

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling `up`, `down`, `left` or `right`, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position \(excluded\) to the destination \(included\). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

1.There is only one ball and one destination in the maze.  
2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.  
3.The given maze does not contain border \(like the red rectangle in the example pictures\), but you could assume the border of the maze are all walls.  
4.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.Example

```text
Example 1:
	Input:  
	(rowStart, colStart) = (0,4)
	(rowDest, colDest)= (4,4)
	0 0 1 0 0
	0 0 0 0 0
	0 0 0 1 0
	1 1 0 1 1
	0 0 0 0 0

	Output:  12
	
	Explanation:
	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(2,0)->(2,1)->(2,2)->(3,2)->(4,2)->(4,3)->(4,4)

Example 2:
	Input:
	(rowStart, colStart) = (0,4)
	(rowDest, colDest)= (0,0)
	0 0 1 0 0
	0 0 0 0 0
	0 0 0 1 0
	1 1 0 1 1
	0 0 0 0 0

	Output:  6
	
	Explanation:
	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(0,0)
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # write your code here
        if not maze or not maze[0]:
            return -1
        ans = float('inf')
        
        start = (start[0], start[1])
        destination = (destination[0], destination[1])
        distances = {start : 0}
        queue = collections.deque([start])
        while queue:
            point = queue.popleft()
            if point == destination:
                ans = min(ans, distances[point])
            next_points = self.get_next_points(maze, point, distances[point])
            for next_point in next_points:
                if next_point in distances:
                    if next_points[next_point] >= distances[next_point]:
                        continue
                distances[next_point] = next_points[next_point]
                queue.append(next_point)
        if ans != float('inf'):
            return ans
        return -1
    
    def get_next_points(self, maze, point, pre_steps):
        next_points= {}
        x, y = point
        m, n = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        for dx, dy in directions:
            new_x, new_y = x, y
            steps = 0
            while 0 <= new_x < m and 0 <= new_y < n and maze[new_x][new_y] == 0:
                new_x, new_y = new_x + dx, new_y + dy
                steps+=1
            next_points[(new_x - dx, new_y - dy)] = pre_steps + steps - 1

        return next_points
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

