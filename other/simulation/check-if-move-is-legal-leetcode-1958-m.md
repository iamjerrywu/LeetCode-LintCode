# Check if Move is Legal (LeetCode 1958) (M)

## Problem

You are given a **0-indexed** `8 x 8` grid `board`, where `board[r][c]` represents the cell `(r, c)` on a game board. On the board, free cells are represented by `'.'`, white cells are represented by `'W'`, and black cells are represented by `'B'`.

Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). However, a move is only **legal** if, after changing it, the cell becomes the **endpoint of a good line** (horizontal, vertical, or diagonal).

A **good line** is a line of **three or more cells (including the endpoints)** where the endpoints of the line are **one color**, and the remaining cells in the middle are the **opposite color** (no cells in the line are free). You can find examples for good lines in the figure below:![](https://assets.leetcode.com/uploads/2021/07/22/goodlines5.png)

Given two integers `rMove` and `cMove` and a character `color` representing the color you are playing as (white or black), return `true` _if changing cell_ `(rMove, cMove)` _to color_ `color` _is a **legal** move, or_ `false` _if it is not legal_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/07/10/grid11.png)

```
Input: board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"
Output: true
Explanation: '.', 'W', and 'B' are represented by the colors blue, white, and black respectively, and cell (rMove, cMove) is marked with an 'X'.
The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/07/10/grid2.png)

```
Input: board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"
Output: false
Explanation: While there are good lines with the chosen cell as a middle cell, there are no good lines with the chosen cell as an endpoint.
```

**Constraints:**

* `board.length == board[r].length == 8`
* `0 <= rMove, cMove < 8`
* `board[rMove][cMove] == '.'`
* `color` is either `'B'` or `'W'`.

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        
        board[rMove][cMove] = color
        
        for direction in DIRECTIONS:
            if self.has_good_cell(rMove, cMove, color, direction, board):
                return True
        return False
    
    def has_good_cell(self, x, y, color, direction, board):
        n, m = len(board), len(board[0])
        dx, dy = direction
        x, y = x + dx, y + dy
        length = 1
        while 0 <= x < n and 0 <= y < m:
            length +=1
            if board[x][y] == '.':
                return False
            if board[x][y] == color:
                return length >= 3
            x, y = x + dx, y + dy
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
