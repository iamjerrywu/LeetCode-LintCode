# Minesweaper (LeetCode 529) (M)

## Problem

Let's play the minesweeper game ([Wikipedia](https://en.wikipedia.org/wiki/Minesweeper\_\(video\_game\)), [online game](http://minesweeperonline.com/))!

You are given an `m x n` char matrix `board` representing the game board where:

* `'M'` represents an unrevealed mine,
* `'E'` represents an unrevealed empty square,
* `'B'` represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
* digit (`'1'` to `'8'`) represents how many mines are adjacent to this revealed square, and
* `'X'` represents a revealed mine.

You are also given an integer array `click` where `click = [clickr, clickc]` represents the next click position among all the unrevealed squares (`'M'` or `'E'`).

Return _the board after revealing this position according to the following rules_:

1. If a mine `'M'` is revealed, then the game is over. You should change it to `'X'`.
2. If an empty square `'E'` with no adjacent mines is revealed, then change it to a revealed blank `'B'` and all of its adjacent unrevealed squares should be revealed recursively.
3. If an empty square `'E'` with at least one adjacent mine is revealed, then change it to a digit (`'1'` to `'8'`) representing the number of adjacent mines.
4. Return the board when no more squares will be revealed.

**Example 1:**![](https://assets.leetcode.com/uploads/2018/10/12/minesweeper\_example\_1.png)

```
Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
```

**Example 2:**![](https://assets.leetcode.com/uploads/2018/10/12/minesweeper\_example\_2.png)

```
Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
```

**Constraints:**

* `m == board.length`
* `n == board[i].length`
* `1 <= m, n <= 50`
* `board[i][j]` is either `'M'`, `'E'`, `'B'`, or a digit from `'1'` to `'8'`.
* `click.length == 2`
* `0 <= clickr < m`
* `0 <= clickc < n`
* `board[clickr][clickc]` is either `'M'` or `'E'`.

## Solution - DFS

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1,-1]]
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        self.dfs(x, y, board, set())
        return board
    
    def dfs(self, x, y, board, visited):
        adj_mines = 0
        empty_list = []
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if self.is_valid(new_x, new_y, board, visited):
                if board[new_x][new_y] == 'M':
                    adj_mines+=1
                elif board[new_x][new_y] == 'E':
                    # can only first add into empty list, since we don't know 
                    # whether current x, y has adjacent mines
                    empty_list.append((new_x, new_y))                
        if adj_mines:
            board[x][y] = str(adj_mines)
            return 
        else:
            board[x][y] = 'B'
            visited.add((x, y))
            for x, y in empty_list:
                self.dfs(x, y, board, visited)
    
    def is_valid(self, x, y, board, visited):
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            return (x, y) not in visited
        return False
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**

****

## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
import collections
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1,-1]]
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        queue = collections.deque([(x, y)])
        self.bfs(x, y, board, queue, set())
        return boardz
    
    def bfs(self, x, y, board, queue, visited):
        while queue:
            x, y = queue.popleft()
            # Since in BFS, points may added duplicated, could check first with visited, to save time
            if (x, y) in visited:
                continue
            visited.add((x, y))
            adj_mines = 0
            empty_list = []
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if self.is_valid(new_x, new_y, board, visited):
                    if board[new_x][new_y] == 'M':
                        adj_mines+=1
                    elif board[new_x][new_y] == 'E':
                        empty_list.append((new_x, new_y))                
            if adj_mines:
                board[x][y] = str(adj_mines)
            else:
                board[x][y] = 'B'
                for new_x, new_y in empty_list:
                    queue.append((new_x, new_y))
    
    def is_valid(self, x, y, board, visited):
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            return (x, y) not in visited
        return False
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**

## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
import collections
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1,-1]]
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        queue = collections.deque([(x, y)])
        self.bfs(x, y, board, queue, set())
        return board
    
    def bfs(self, x, y, board, queue, visited):
        while queue:
        
            x, y = queue.popleft()
            # visited add here is bad! since later 
            # Since in BFS, points may added duplicated, could check first with visited, to save time
            
            adj_mines = 0
            empty_list = []
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if self.is_valid(new_x, new_y, board, visited):
                    if board[new_x][new_y] == 'M':
                        adj_mines+=1
                    elif board[new_x][new_y] == 'E':
                        empty_list.append((new_x, new_y))                
            if adj_mines:
                board[x][y] = str(adj_mines)
            else:
                board[x][y] = 'B'
                for new_x, new_y in empty_list:
                    queue.append((new_x, new_y))
                    # visited add here is much better
                    visited.add((new_x, new_y))
    
    def is_valid(self, x, y, board, visited):
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            return (x, y) not in visited
        return False
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
