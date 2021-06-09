# Sudoku Solver 802 \(H\)

## Problem

Description

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the number `0`.

You may assume that there will be only one unique solution.Example

**Example 1:**

```text
Given a Sudoku puzzle:[[0,0,9,7,4,8,0,0,0],[7,0,0,0,0,0,0,0,0],[0,2,0,1,0,9,0,0,0],[0,0,7,0,0,0,2,4,0],[0,6,4,0,1,0,5,9,0],[0,9,8,0,0,0,3,0,0],[0,0,0,8,0,3,0,2,0],[0,0,0,0,0,0,0,0,6],[0,0,0,2,7,5,9,0,0]]
```

![](https://lintcode-media.s3.amazonaws.com/problem/250px-Sudoku-by-L2G-20050714.svg.png)

```text
Return its solution:[[5,1,9,7,4,8,6,3,2],[7,8,3,6,5,2,4,1,9],[4,2,6,1,3,9,8,7,5],[3,5,7,9,8,6,2,4,1],[2,6,4,3,1,7,5,9,8],[1,9,8,5,2,4,3,6,7],[9,7,5,8,6,3,1,2,4],[8,3,2,4,9,1,7,5,6],[6,4,1,2,7,5,9,8,3]]
```

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

* **Time Complexity:**O\(n ^ m\) 
  * where n is the number of possibilities for each square \(i.e., 9 in classic Sudoku\) and m is the number of spaces that are blank.
  * The problem can be designed for a grid size of N\*N where N is a perfect square. For such an N, let M = N\*N, the recurrence equation can be written as T\(M\) = 9\*T\(M-1\) + O\(1\), where T\(N\) is the running time of the solution for a problem size of N. Solving this recurrence will yield, O\(9^M\).
* **Space Complexity O\(m\):**
  * it’s the recursion stack that is used as an auxiliary space which is N\*N step deep. 
  * Remember we need to fill in 81 cells in a 9\*9 sudoku and at each level, only one cell is filled. So, space complexity would be **O\(M\)**.

