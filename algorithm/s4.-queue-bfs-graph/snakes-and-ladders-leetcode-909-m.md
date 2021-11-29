# Snakes and Ladders (LeetCode 909) (M)

## Problem

You are given an `n x n` integer matrix `board` where the cells are labeled from `1` to `n2` in a [**Boustrophedon style**](https://en.wikipedia.org/wiki/Boustrophedon) starting from the bottom left of the board (i.e. `board[n - 1][0]`) and alternating direction each row.

You start on square `1` of the board. In each move, starting from square `curr`, do the following:

* Choose a destination square `next` with a label in the range `[curr + 1, min(curr + 6, n2)]`.
  * This choice simulates the result of a standard **6-sided die roll**: i.e., there are always at most 6 destinations, regardless of the size of the board.
* If `next` has a snake or ladder, you **must** move to the destination of that snake or ladder. Otherwise, you move to `next`.
* The game ends when you reach the square `n2`.

A board square on row `r` and column `c` has a snake or ladder if `board[r][c] != -1`. The destination of that snake or ladder is `board[r][c]`. Squares `1` and `n2` do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do **not** follow the subsequent snake or ladder.

* For example, suppose the board is `[[-1,4],[-1,3]]`, and on the first move, your destination square is `2`. You follow the ladder to square `3`, but do **not** follow the subsequent ladder to `4`.

Return _the least number of moves required to reach the square_ `n2`_. If it is not possible to reach the square, return_ `-1`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/09/23/snakes.png)

```
Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
```

**Example 2:**

```
Input: board = [[-1,-1],[-1,3]]
Output: 1
```

&#x20;

**Constraints:**

* `n == board.length == board[i].length`
* `2 <= n <= 20`
* `grid[i][j]` is either `-1` or in the range `[1, n2]`.
* The squares labeled `1` and `n2` do not have any ladders or snakes

## Solution

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = collections.deque([1])
        steps = 0
        visited = set([1])
        while queue:
            for _ in range(len(queue)):
                pos = queue.popleft()
                if pos == n ** 2:
                    return steps
                for d in range(1, 7):
                    new_pos = pos + d
                    # should check here since only if it's in range, then we can transform it into coordination
                    if new_pos > n ** 2:
                        continue
                    x, y = self.pos_to_cor(new_pos, n)
                    # ladder or snake
                    if board[x][y] != -1:
                        x, y = self.pos_to_cor(board[x][y], n)
                    new_pos = self.cor_to_pos(x, y, n)
                    # check visited here, since the last positioin (new_pos) is what we care 
                    if new_pos not in visited:
                        queue.append(new_pos)
                        visited.add(new_pos)
            steps+=1
        return -1
    
    def pos_to_cor(self, pos, n):
        x = n - 1 - (pos - 1)//n
        if (n%2 == 0 and x%2 == 1) or (n%2 == 1 and x%2 == 0): 
            y = (pos - 1)%n
        else:
            y = n - 1 - (pos - 1)%n
        return x, y
    
    def cor_to_pos(self, x, y, n):
        if (n%2 == 0 and x%2 == 1) or (n%2 == 1 and x%2 == 0): 
            return n * (n - 1 - x) + y + 1    
        else:
            return n * (n - 1 - x) + (n - y)
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n \* n)**
* **Space Complexity: O(n)**
