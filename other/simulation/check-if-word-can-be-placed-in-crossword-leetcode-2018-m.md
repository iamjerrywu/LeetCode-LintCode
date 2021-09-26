# Check if Word Can Be Placed In Crossword \(LeetCode 2018\) \(M\)

## Problem



You are given an `m x n` matrix `board`, representing the **current** state of a crossword puzzle. The crossword contains lowercase English letters \(from solved words\), `' '` to represent any **empty** cells, and `'#'` to represent any **blocked** cells.

A word can be placed **horizontally** \(left to right **or** right to left\) or **vertically** \(top to bottom **or** bottom to top\) in the board if:

* It does not occupy a cell containing the character `'#'`.
* The cell each letter is placed in must either be `' '` \(empty\) or **match** the letter already on the `board`.
* There must not be any empty cells `' '` or other lowercase letters **directly left or right** of the word if the word was placed **horizontally**.
* There must not be any empty cells `' '` or other lowercase letters **directly above or below** the word if the word was placed **vertically**.

Given a string `word`, return `true` _if_ `word` _can be placed in_ `board`_, or_ `false` _**otherwise**_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/09/18/crossword-1.png)

```text
Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
Output: true
Explanation: The word "abc" can be placed as shown above (top to bottom).
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/09/18/c2.png)

```text
Input: board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
Output: false
Explanation: It is impossible to place the word because there will always be a space/letter above or below it.
```

**Example 3:**![](https://assets.leetcode.com/uploads/2021/09/18/crossword-2.png)

```text
Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
Output: true
Explanation: The word "ca" can be placed as shown above (right to left). 
```

**Constraints:**

* `m == board.length`
* `n == board[i].length`
* `1 <= m * n <= 2 * 105`
* `board[i][j]` will be `' '`, `'#'`, or a lowercase English letter.
* `1 <= word.length <= max(m, n)`
* `word` will contain only lowercase English letters.

## Solution

Pay attention that the word actually doesn't need to fit in in order, but can be scattered randomly.

{% tabs %}
{% tab title="Python" %}
```python
import collections 
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        # construct horizontal list
        word_cnt = collections.Counter(word)
        n, m = len(board), len(board[0])
        horizontal_list = [[] for _ in range(n)]
        w_len = len(word)
        for i in range(n):
            cnt = 0
            prev = 0
            for j in range(m):
                if board[i][j] != '#':
                    if j == 0 or board[i][j - 1] == '#':
                        start = j
                        
                    prev = j
                    cnt+=1
                if j != prev:
                    if cnt == w_len:
                        horizontal_list[i].append([start, start + cnt])
                    cnt = 0
            if cnt == w_len:
                horizontal_list[i].append([start, start + cnt])
        
        # construct vertical list
        vertical_list = [[] for _ in range(m)]
        w_len = len(word)
        for j in range(m):
            cnt = 0
            prev = 0
            for i in range(n):
                if board[i][j] != '#':
                    if i == 0 or board[i - 1][j] == '#':
                        start = i
                    prev = i
                    cnt+=1
                if i != prev:
                    if cnt == w_len:
                        vertical_list[j].append([start, start + cnt])
                    cnt = 0
            if cnt == w_len:
                vertical_list[j].append([start, start + cnt])
        
        # check vertical list
        for j in range(len(vertical_list)):
            for start, end in vertical_list[j]:
                if self.can_fit(start, end, board, word_cnt, j, False):
                    return True
        
        # check horizontal list
        for i in range(len(horizontal_list)):
            for start, end in horizontal_list[i]:
                if self.can_fit(start, end, board, word_cnt, i, True):
                    return True
        return False
    
    
    def can_fit(self, start, end, board, word_cnt, idx, is_horizontal):
        b_cnt = {}
        if is_horizontal:
            for j in range(start, end):
                if board[idx][j] != ' ':
                    b_cnt[board[idx][j]] = b_cnt.get(board[idx][j], 0) + 1
            for k, v in b_cnt.items():
                if k not in word_cnt:
                    return False
                if v > word_cnt[k]:
                    return False
            return True
            
        else:
            for i in range(start, end):
                if board[i][idx] != ' ':
                    b_cnt[board[i][idx]] = b_cnt.get(board[i][idx], 0) + 1
            for k, v in b_cnt.items():
                if k not in word_cnt:
                    return False
                if v > word_cnt[k]:
                    return False
            return True
```
{% endtab %}
{% endtabs %}

* **Time Complexity:** 
* **Space Complexity:**

