# Count Square Submatrices with All Ones 1869 \(M\)

## Problem

Given a m \* n matrix of ones and zeros, please count and return the number of square submatrix completely composed of 1.

* 1 &lt;= arr.length &lt;= 300
* 1 &lt;= arr\[0\].length &lt;= 300

Example

**Example 1:**

```text
Input: matrix =[  [0,1,1,1],  [1,1,1,1],  [0,1,1,1]]Output: 15Explanation: There are 10 squares of side 1.There are 4 squares of side 2.There is  1 square of side 3.Total number of squares = 10 + 4 + 1 = 15.
```

**Example 2:**

```text
Input: matrix = [  [1,0,1],  [1,1,0],  [1,1,0]]Output: 7Explanation: There are 6 squares of side 1.  There is 1 square of side 2. Total number of squares = 6 + 1 = 7.
```

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param matrix: a matrix
    @return: return how many square submatrices have all ones
    """
    def countSquares(self, matrix):
        # write your code here
        n, m = len(matrix), len(matrix[0])
        
        # state: dp[i][j] means how 1*1 squares that i, j as right bottom square
        # state: left[i][j] means i, j to left, the longest length of consecutive 1
        # state: left[i][j] means i, j to up, the longest length of consecutive 1

        dp = [[0] * m for _ in range(n)]
        left = [[0] * m for _ in range(n)]
        up = [[0] * m for _ in range(n)]
        
        # init: init first line
        for i in range(n):
            dp[i][0] = left[i][0] = up[i][0] = matrix[i][0]
        for j in range(m):
            dp[0][j] = left[0][j] = up[0][j] = matrix[0][j]
        
        # function: if matrix[i][j] = 0, then dp[i][j] = 0; otherwise, 
        #    dp[i][j] = min(left[i][j - 1], up[i - 1][j], dp[i - 1][j - 1]) + 1
        #    can also write as:
        #    dp[i][j] = min(left[i][j], up[i][j], dp[i - 1][j - 1] + 1)

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    continue
                left[i][j] = left[i][j - 1] + 1
                up[i][j] = up[i - 1][j] + 1
                dp[i][j] = min(left[i][j - 1], up[i - 1][j], dp[i - 1][j - 1]) + 1
        
        ans = 0
        for i in range(n):
            ans+=sum(dp[i])
        return ans
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* m\)**
* **Space Complexity: O\(n \* m\)**

## Solution - DP with strolling arrays

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param matrix: a matrix
    @return: return how many square submatrices have all ones
    """
    def countSquares(self, matrix):
        # write your code here
        n, m = len(matrix), len(matrix[0])
        
        # state: dp[i][j] means how 1*1 squares that i, j as right bottom square
        # state: left[i][j] means i, j to left, the longest length of consecutive 1
        # state: left[i][j] means i, j to up, the longest length of consecutive 1

        dp = [[0] * m for _ in range(2)]
        left = [[0] * m for _ in range(2)]
        up = [[0] * m for _ in range(2)]
        
        # init: init first line
        # for i in range(n):
        #     dp[i][0] = left[i][0] = up[i][0] = matrix[i][0]
        
        # init first row
        for j in range(m):
            dp[0][j] = left[0][j] = up[0][j] = matrix[0][j]
        ans = sum(dp[0])
        
        # function: if matrix[i][j] = 0, then dp[i][j] = 0; otherwise, 
        #    dp[i][j] = min(left[i][j - 1], up[i - 1][j], dp[i - 1][j - 1]) + 1
        #    can also write as:
        #    dp[i][j] = min(left[i][j], up[i][j], dp[i - 1][j - 1] + 1)

        for i in range(1, n):
            dp[i%2][0] = left[i%2][0] = up[i%2][0] = matrix[i][0]
            for j in range(1, m):
                if matrix[i][j] == 0:
                    dp[i%2][j] = left[i%2][j] = up[i%2][j] = 0
                    continue
                left[i%2][j] = left[i%2][j - 1] + 1
                up[i%2][j] = up[(i - 1)%2][j] + 1
                dp[i%2][j] = min(left[i%2][j - 1], up[(i - 1)%2][j], dp[(i - 1)%2][j - 1]) + 1
            ans+=sum(dp[i%2])
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* m\)**
* **Space Complexity: O\(m\)**

