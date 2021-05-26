# The Maze III 789 \(M\)

## Problem

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling `up (u)`, `down (d)`, `left (l)` or `right (r)`, `but it won't stop rolling until hitting a wall`. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the position of the ball, the position of the hole and the maze, find out how the ball falls into the hole by moving the `shortest distance`. The distance is defined by the number of empty spaces the ball passes from the starting position \(excluded\) to the hole \(included\). `Use "u", "d", "l" and "r" to output the direction of movement`. Since there may be several different shortest paths, you should output the shortest method in alphabetical order. If the ball doesn't go into the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.

1.There is only one ball and one hole in the maze. 2.Both the ball and hole exist on an empty space, and they will not be at the same position initially. 3.The given maze does not contain border \(like the red rectangle in the example pictures\), but you could assume the border of the maze are all walls. 4.The maze contains at least 2 empty spaces, and the width and the height of the maze won't exceed 30.Example

**Example 1:**

```text
Input:[[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]][4,3][0,1]Output:"lul"
```

**Example 2:**

```text
Input:[[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]][0,0][1,1][2,2][3,3]Output:"impossible"
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

