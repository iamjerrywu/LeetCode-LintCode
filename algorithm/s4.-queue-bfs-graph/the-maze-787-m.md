# The Maze 787 \(M\)

## Problem

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling `up`, `down`, `left` or `right`, `but it won't stop rolling until hitting a wall`. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

1.There is only one ball and one destination in the maze.  
2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.  
3.The given maze does not contain border \(like the red rectangle in the example pictures\), but you could assume the border of the maze are all walls.  
5.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.Example

Example 1:

```text
Input:map = [ [0,0,1,0,0], [0,0,0,0,0], [0,0,0,1,0], [1,1,0,1,1], [0,0,0,0,0]]start = [0,4]end = [3,2]Output:false
```

Example 2:

```text
Input:map = [[0,0,1,0,0], [0,0,0,0,0], [0,0,0,1,0], [1,1,0,1,1], [0,0,0,0,0]]start = [0,4]end = [4,4]Output:tru
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        if not maze or not maze[0]:
            return False
        
        start = (start[0], start[1])
        destination = (destination[0], destination[1])
        queue = collections.deque()
        visited = set()
        queue.append(start)
        visited.add(start)

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                next_pos = self.find_next_pos(x, y, dx, dy, maze, visited)
                if next_pos == (-1, -1):
                    continue
                if next_pos == destination:
                    return True
                queue.append(next_pos)
                visited.add(next_pos)
        return False
    
    def find_next_pos(self, x, y, dx, dy, maze, visited):
        m, n = len(maze), len(maze[0])
        while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
            x+=dx
            y+=dy
        return (x, y) if (x, y) not in visited else (-1, -1)   
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

