# Sudoku Solver 802 (H)

## Problem



Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

&#x20;

**Example 1:**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

```
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

```

&#x20;

**Constraints:**

* `board.length == 9`
* `board[i].length == 9`
* `board[i][j]` is a digit or `'.'`.
* It is **guaranteed** that the input board has only one solution.

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
            # traverse the same row
            if board[x][i] == val:
                return False
            # traverse the same column
            if board[i][y] == val:
                return False
            # check the 3 * 3 block, whether same value exist already
            if board[x//3 * 3 + i//3][y//3 * 3 + i%3] == val:
                return False
        return True       

    def dfs(self, board, index):
        if index == 81:
            return True
        x, y = index//9, index%9
        # if not zero, continue to next point (index + 1)
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

* **Time Complexity:**O(n ^ m)&#x20;
  * where n is the number of possibilities for each square (i.e., 9 in classic Sudoku) and m is the number of spaces that are blank.
  * The problem can be designed for a grid size of N\*N where N is a perfect square. For such an N, let M = N\*N, the recurrence equation can be written as T(M) = 9\*T(M-1) + O(1), where T(N) is the running time of the solution for a problem size of N. Solving this recurrence will yield, O(9^M).
* **Space Complexity O(m):**
  * it’s the recursion stack that is used as an auxiliary space which is N\*N step deep.&#x20;
  * Remember we need to fill in 81 cells in a 9\*9 sudoku and at each level, only one cell is filled. So, space complexity would be **O(M)**.



## Approach - Brute Force DFS

### Intuition

Brute force DFS traverse every place on the board. (using x/y as coordination)

### Algorithm

#### Step by Step

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(0, 0, board)
        return board
    
    def dfs(self, i, j, board):
        if j == 9:
            return True
        nxt_i = (i + 1)%9
        nxt_j = j if i < 8 else j + 1
        if board[i][j] != '.':
            # nxt_i = (i + 1)%9
            # nxt_j = j if i < 8 else j + 1
            return self.dfs(nxt_i, nxt_j, board)
        
        for num in range(1, 10):
            if self.is_valid(i, j, num, board):
                board[i][j] = str(num)
                if self.dfs(nxt_i, nxt_j, board):
                    return True
                board[i][j] = '.'
        return False
    
    def is_valid(self, x, y, num, board):
        for i in range(9):
            if board[i][y] == str(num):
                return False
        for j in range(9):
            if board[x][j] == str(num):
                return False
        for k in range(9):
            if board[(x//3) * 3 + k//3][(y//3) * 3 + k%3] == str(num):
                return False
        return True
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**O(n ^ m)&#x20;
* **Space Complexity O(m):**
