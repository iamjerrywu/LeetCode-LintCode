# Sudoku Solver 802 \(H\)

## Problem

### Description

### Example

## Approach - Brute Force DFS

### Intuition

Brute force DFS traverse every place on the board.

### Algorithm

#### Step by Step

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        # write your code here
        self.dfs(board, 0)
    
    def is_valid(self, board, x, y, val):
        for i in range(9):
            if board[x][i] == val:
                return False
            if board[i][y] == val:
                return False
            if board[x//3 * 3 + i//3][y//3 * 3 + i%3] == val:
                return False
        return True       

    def dfs(self, board, index):
        if index == 81:
            return True
        x, y = index//9, index%9
        if board[x][y] != 0:
            return self.dfs(board, index + 1)
        # 1 ~ 9 value
        for val in range(1, 10):
            if not self.is_valid(board, x, y, val):
                continue
        
            board[x][y] = val
            if self.dfs(board, index + 1):
                return True
            board[x][y] = 0
        return False


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

