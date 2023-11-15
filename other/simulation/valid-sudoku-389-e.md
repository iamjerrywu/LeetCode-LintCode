# Valid Sudoku 389 (E)

## Problem

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.

**Example 1:**![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Example 2:**

```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

**Constraints:**

* `board.length == 9`
* `board[i].length == 9`
* `board[i][j]` is a digit or `'.'`.



## Solution - Brute Force Suduku Solver Sol.

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not self.is_valid(i, j, board[i][j], board):
                    return False
        return True
    
    def is_valid(self, row, col, num, board):
        if board[row][col] == '.':
            return True
        
        # exclude board[row][col] itself
        for i in range(9):
            if i != row and board[i][col] == num:
                return False
        for j in range(9):
            if j != col and board[row][j] == num:
                return False
        for k in range(9):
            n_row = row//3 * 3 + k//3
            n_col = col//3 * 3 + k%3
            if n_row != row and n_col != col and board[row//3 * 3 + k//3][col//3 * 3 + k%3] == num:
                return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**



## Solution - Brute Force Suduku Solver Sol.

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not self.is_valid(i, j, board[i][j], board):
                    return False
        return True
    
    def is_valid(self, row, col, num, board):
        if board[row][col] == '.':
            return True
        
        # exclude board[row][col] itself
        for i in range(9):
            if i != row and board[i][col] == num:
                return False
        for j in range(9):
            if j != col and board[row][j] == num:
                return False
        for k in range(9):
            n_row = row//3 * 3 + k//3
            n_col = col//3 * 3 + k%3
            if n_row != row and n_col != col and board[row//3 * 3 + k//3][col//3 * 3 + k%3] == num:
                return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):
        # write your code here
        record = set()
        for i in range(len(board)):
            record.clear()
            if not self.check_rows(i, board, record):
                return False
        for j in range(len(board[0])):
            record.clear()
            if not self.check_columns(j, board, record):
                return False
        for i in range(3):
            for j in range(3):
                record.clear()
                if not self.check_sub_blocks(i, j, board, record):
                    return False
        return True
    
    def check_rows(self, index, board, record):
        for j in range(len(board[0])):
            if board[index][j] == '.':
                continue
            if board[index][j] not in record:
                record.add(board[index][j])
            else:
                return False
        return True
    
    def check_columns(self, index, board, record):
        for i in range(len(board)):
            if board[i][index] == '.':
                continue
            if board[i][index] not in record:
                record.add(board[i][index])
            else:
                return False
        return True
    
    def check_sub_blocks(self, i, j, board, record):
        for k in range(9):
            if board[i * 3 + k//3][j * 3 + k%3] == '.':
                continue
            if board[i * 3 + k//3][j * 3 + k%3] not in record:
                record.add(board[i * 3 + k//3][j * 3 + k%3])
            else:
                return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^2)**
* **Space Complexity:** O(1) (Reuse)

