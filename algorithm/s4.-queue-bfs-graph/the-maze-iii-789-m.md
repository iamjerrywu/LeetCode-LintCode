# The Maze III 789 (H)

## Problem

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling `up (u)`, `down (d)`, `left (l)` or `right (r)`, `but it won't stop rolling until hitting a wall`. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the position of the ball, the position of the hole and the maze, find out how the ball falls into the hole by moving the `shortest distance`. The distance is defined by the number of empty spaces the ball passes from the starting position (excluded) to the hole (included). `Use "u", "d", "l" and "r" to output the direction of movement`. Since there may be several different shortest paths, you should output the shortest method in alphabetical order. If the ball doesn't go into the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.

1.There is only one ball and one hole in the maze. 2.Both the ball and hole exist on an empty space, and they will not be at the same position initially. 3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls. 4.The maze contains at least 2 empty spaces, and the width and the height of the maze won't exceed 30.Example

**Example 1:**

```
Input:[[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]][4,3][0,1]Output:"lul"
```

**Example 2:**

```
Input:[[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]][0,0][1,1][2,2][3,3]Output:"impossible"
```

## Solution - BFS

### Code

{% tabs %}
{% tab title="python" %}
```python
DIRECTION_HASH = {
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
}

class MazeGridType:
    SPACE = 0
    WALL = 1
class Solution:
    """
    @param maze: the maze
    @param ball: the ball position
    @param hole: the hole position
    @return: the lexicographically smallest way
    """
    def findShortestWay(self, maze, ball, hole):
        # write your code here
        
        # corner case check
        if not ball or not hole:
            return 'impossible'
        if not maze or not maze[0]:
            return 'impossible'
        
        hole = (hole[0], hole[1])

        #(distance, x, y, path)
        queue = collections.deque([(ball[0], ball[1])])
        distance = {(ball[0], ball[1]): (0, '')}

        while queue:
            x, y = queue.popleft()
            dist, path = distance[(x, y)]
            for direction in DIRECTION_HASH:
                # if previous action is 'l', then cannot choose 'l' again
                if path and path[-1] == direction:
                    continue
                new_x, new_y = self.kick_ball(x, y, direction, maze, hole)
                new_dist = dist + abs(new_x - x) + abs(new_y - y)
                new_path = path + direction 
                if (new_x, new_y) in distance and distance[(new_x, new_y)] <= (new_dist, new_path):
                    continue
                
                queue.append((new_x, new_y))
                distance[(new_x, new_y)] = (new_dist, new_path)
        
        return distance[hole][1] if hole in distance else 'impossible'

    def kick_ball(self, x, y, direction, maze, hole):
        # kick ball through direction from x, y and return the stopped position
        dx, dy = DIRECTION_HASH[direction]
        while (x, y) != hole and not self.is_wall(x, y, maze):
            x+=dx
            y+=dy
        if (x, y) == hole:
            return x, y
        
        return x - dx, y - dy
    
    def is_wall(self, x, y, maze):
        # when position out of boundary, counsider as well as well
        if not (0 <= x < len(maze)) or not (0 <= y < len(maze[0])):
            return True
        
        return maze[x][y] == MazeGridType.WALL
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**



## Solution - BFS with Heap Optimization (SPFA)

### Code

{% tabs %}
{% tab title="python" %}
```python
DIRECTION_HASH = {
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
}

class MazeGridType:
    SPACE = 0
    WALL = 1
import heapq
class Solution:
    """
    @param maze: the maze
    @param ball: the ball position
    @param hole: the hole position
    @return: the lexicographically smallest way
    """
    def findShortestWay(self, maze, ball, hole):
        # write your code here
        
        # corner case check
        if not ball or not hole:
            return 'impossible'
        if not maze or not maze[0]:
            return 'impossible'
        
        hole = (hole[0], hole[1])

        #(distance, x, y, path)
        queue = [(0, '', ball[0], ball[1])]
        distance = {(ball[0], ball[1]): (0, '')}

        while queue:
            dist, path, x, y = heapq.heappop(queue)
            for direction in DIRECTION_HASH:
                # if previous action is 'l', then cannot choose 'l' again
                if path and path[-1] == direction:
                    continue
                new_x, new_y = self.kick_ball(x, y, direction, maze, hole)
                new_dist = dist + abs(new_x - x) + abs(new_y - y)
                new_path = path + direction 
                if (new_x, new_y) in distance and distance[(new_x, new_y)] <= (new_dist, new_path):
                    continue
                
                heapq.heappush(queue, (new_dist, new_path, new_x, new_y))
                distance[(new_x, new_y)] = (new_dist, new_path)
        
        return distance[hole][1] if hole in distance else 'impossible'

    def kick_ball(self, x, y, direction, maze, hole):
        # kick ball through direction from x, y and return the stopped position
        dx, dy = DIRECTION_HASH[direction]
        while (x, y) != hole and not self.is_wall(x, y, maze):
            x+=dx
            y+=dy
        if (x, y) == hole:
            return x, y
        
        return x - dx, y - dy
    
    def is_wall(self, x, y, maze):
        # when position out of boundary, counsider as well as well
        if not (0 <= x < len(maze)) or not (0 <= y < len(maze[0])):
            return True
        
        return maze[x][y] == MazeGridType.WALL
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
