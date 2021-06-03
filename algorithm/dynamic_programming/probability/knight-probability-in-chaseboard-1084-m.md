# Knight Probability in Chaseboard 1084 \(M\)

## Problem



On an `n x n` chessboard, a knight starts at the cell `(row, column)` and attempts to make exactly `k` moves. The rows and columns are **0-indexed**, so the top-left cell is `(0, 0)`, and the bottom-right cell is `(n - 1, n - 1)`.

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.![](https://assets.leetcode.com/uploads/2018/10/12/knight.png)

Each time the knight is to move, it chooses one of eight possible moves uniformly at random \(even if the piece would go off the chessboard\) and moves there.

The knight continues moving until it has made exactly `k` moves or has moved off the chessboard.

Return _the probability that the knight remains on the board after it has stopped moving_.

**Example 1:**

```text
Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
```

**Example 2:**

```text
Input: n = 1, k = 0, row = 0, column = 0
Output: 1.00000
```

**Constraints:**

* `1 <= n <= 25`
* `0 <= k <= 100`
* `0 <= row, column <= n`

## Solution 

Cannot depend on the valid points and invalid points based on Traverse \(BFS/DFS\) solution. Since the probability on every point during the process is different 

### Code

{% tabs %}
{% tab title="python" %}
```python
DIRECTIONS = [(1,2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
class Solution:
    """
    @param N: int
    @param K: int
    @param r: int
    @param c: int
    @return: the probability
    """
    def knightProbability(self, N, K, r, c):
        # Write your code here.
        dp = [[[0] * (K + 1) for i in range(N)] for j in range(N)]

        # init
        dp[r][c][0] = 1

        for k in range(1, K + 1):
            for i in range(N):
                for j in range(N):
                    for delta_x, delta_y in DIRECTIONS:
                        last_x = i + delta_x
                        last_y = j + delta_y
                        if self.is_valid(last_x, last_y, N):
                            dp[i][j][k]+=dp[last_x][last_y][k - 1]*0.125
        res = 0
        for i in range(N):
            for j in range(N):
                res+=dp[i][j][K]
        return res
    
    def is_valid(self, i, j, N):
        if i < 0 or i >= N or j < 0 or j >= N:
            return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

