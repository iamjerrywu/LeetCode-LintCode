# Word Search 123 (M)

## Problem

Given a 2D board and a string word, find if the string word exists in the grid.

The string word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.

The same letter cell may not be used more than once.

The dimension of the letter matrix does not exceed 100, and the length of the string does not exceed 100.Example

**Example 1:**

Input:

```
board = ["ABCE","SFCS","ADEE"]word = "ABCCED"
```

Output:

```
true
```

Explanation:

\[\
A B C E\
S F C S\
A D E E\
]\
(0,0)->(0,1)->(0,2)->(1,2)->(2,2)->(2,1)

**Example 1:**

Input:

```
board = ["z"]word = "z"
```

Output:

```
true
```

Explanation:

\[ z ]\
(0,0)

## Solution - DFS

### Code

{% tabs %}
{% tab title="python" %}
```python
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        if not word:
            return True

        prefix_words = self.get_prefix_words(word)
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited.add((i, j))
                if self.dfs(i, j, board, board[i][j], word, prefix_words, visited):
                    return True
                visited.remove((i, j))
        return False
    
    def dfs(self, x, y, board, cur_word, word, prefix_words, visited):
        print(cur_word)
        if cur_word not in prefix_words:
            return False
        if len(cur_word) >= len(word):
            return True
        for dx, dy in DIRECTIONS:
            new_x = x + dx
            new_y = y + dy
            if not self.is_valid(new_x, new_y, board, visited):
                continue
            visited.add((new_x, new_y))
            if self.dfs(new_x, new_y, board, cur_word + board[new_x][new_y], word, prefix_words, visited):
                return True
            visited.remove((new_x, new_y))
        return False

    def is_valid(self, x, y, board, visited):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or (x, y) in visited:
            return False
        return True   
    
    def get_prefix_words(self, word):
        prefix_words = set()
        for i in range(len(word)):
            prefix_words.add(word[:i + 1])
        return prefix_words
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**



## Solution - DFS

### Code

{% tabs %}
{% tab title="python" %}
```python
from collections import deque
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(x, y, k):
            if k == len(word):
                return True
            if not (0 <= x < n and 0 <= y < m and (x, y) not in visited and board[x][y] == word[k]):
                return False
            visited.add((x, y))
            for dx, dy in DIRECTIONS:
                if dfs(x + dx, y + dy, k + 1):
                    return True
            visited.remove((x, y))
            return False
        
        n = len(board)
        m = len(board[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    vector<int> dx = {1, 0, -1, 0};
    vector<int> dy = {0, 1, 0, -1};
    bool exist(vector<vector<char>>& board, string word) {
        if (word.length() == 0) return true;
        if (board.size() == 0 or board[0].size() == 0) return false;
        vector<vector<int>> visited(board.size(), vector<int>(board[0].size(), 0));
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                visited[i][j] = 1;
                if (board[i][j] == word[0] and dfs(i, j, board, visited, 0, word)) 
                    return true;
                visited[i][j] = 0;
            }
        }
        return false;
    }
    
private:
    bool dfs(int x, int y, vector<vector<char>> &board, vector<vector<int>>& visited, int idx, string word) {
        if (idx == word.length() - 1) return true;
        for (int i = 0; i < dx.size(); i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            if (is_valid(new_x, new_y, board, visited, word[idx + 1])) {
                visited[new_x][new_y] = 1;
                if (dfs(new_x, new_y, board, visited, idx + 1, word)) return true;
                visited[new_x][new_y] = 0;
            }
        }
        return false;
    }   

    bool is_valid(int x, int y, vector<vector<char>> &board, vector<vector<int>>& visited, char tar) {
        if (x < 0 or x >= board.size() or y < 0 or y >= board[0].size()) return false;
        if (board[x][y] != tar or visited[x][y]) return false;
        return true;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
