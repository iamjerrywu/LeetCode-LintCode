# Game of Life 1301 \(M\)

## Problem

According to the [Wikipedia's article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life): "The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state _live_ \(1\) or _dead_ \(0\). Each cell interacts with its [eight neighbors](https://en.wikipedia.org/wiki/Moore_neighborhood) \(horizontal, vertical, diagonal\) using the following four rules \(taken from the above Wikipedia article\):

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state \(after one update\) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.Example

**Example :**

```text
Input: [  [0,1,0],  [0,0,1],  [1,1,1],  [0,0,0]]Output: [  [0,0,0],  [1,0,1],  [0,1,1],  [0,1,0]]
```

Challenge

1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

## Solution - Brute Force

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
class Solution:
    """
    @param board: the given board
    @return: nothing
    """
    def gameOfLife(self, board):
        # Write your code here

        m = len(board)
        n = len(board[0])
        next_arr = [[0] * n for _ in range(m)]
        print(next_arr)

        for i in range(m):
            for j in range(n):
                live_cnt = 0
                for dx, dy in DIRECTIONS:
                    new_x = i + dx
                    new_y = j + dy
                    if self.is_live(new_x, new_y, board):
                        live_cnt+=1
                if board[i][j] == 0 and live_cnt == 3:
                    next_arr[i][j] = 1
                elif board[i][j] == 1:
                    if live_cnt == 2 or live_cnt == 3:
                        next_arr[i][j] = 1
                    elif live_cnt > 3:
                        next_arr[i][j] = 0
        
        for i in range(m):
            for j in range(n):
                board[i][j] = next_arr[i][j]
    
    def is_live(self, x, y, board):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        return board[x][y] == 1
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(m \* n\)**
* **Space Complexity: O\(m \* n\)**

\*\*\*\*

## Solution - In Place

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
class Solution:
    """
    @param board: the given board
    @return: nothing
    """
    def gameOfLife(self, board):
        # Write your code here
        
        # Status Representation
        #.    current.   next
        # 00:    dead    dead
        # 01:    live.   dead
        # 10:    dead.   live
        # 11:    live.   live
        
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                live_cnt = 0
                for dx, dy in DIRECTIONS:
                    new_x = i + dx
                    new_y = j + dy
                    if self.is_live(new_x, new_y, board):
                        live_cnt+=1
                if board[i][j] == 0 and live_cnt == 3:
                    board[i][j] = 2
                elif board[i][j] == 1:
                    if live_cnt == 2 or live_cnt == 3:
                        board[i][j] = 3
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>=1
    
    def is_live(self, x, y, board):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        return board[x][y]&1 == 1
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(m \* n\)**
* **Space Complexity: O\(1\)**

