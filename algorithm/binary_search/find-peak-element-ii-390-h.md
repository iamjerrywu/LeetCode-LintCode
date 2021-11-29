# Find Peak Element II 390 (H)

## Problem

Given an integer matrix `A` which has the following features :

* The numbers in adjacent positions are different.
* The matrix has `n` rows and `m` columns, n and m will not less than 3.
* For all `i < n`, `A[i][0] < A[i][1] && A[i][m - 2] > A[i][m - 1]`.
* For all `j < m`, `A[0][j] < A[1][j] && A[n - 2][j] > A[n - 1][j]`

We define a position `[i, j]` is a peak if:

```
  A[i][j] > A[i + 1][j] && A[i][j] > A[i - 1][j] &&   A[i][j] > A[i][j + 1] && A[i][j] > A[i][j - 1]
```

Find a peak element in this matrix. Return the index of the peak.

Guarantee that there is at least one peak, and if there are multiple peaks, return any one of them.Example

**Example 1:**

```
Input:     [      [1, 2, 3, 6,  5],      [16,41,23,22, 6],      [15,17,24,21, 7],      [14,18,19,20,10],      [13,14,11,10, 9]    ]Output: [1,1]Explanation: [2,2] is also acceptable. The element at [1,1] is 41, greater than every element adjacent to it.
```

**Example 2:**

```
Input:     [      [1, 5, 3],      [4,10, 9],      [2, 8, 7]    ]Output: [1,1]Explanation: There is only one peek.
```

Challenge

Solve it in O(n+m) time.

If you come up with an algorithm that you _thought_ it is O(nlogm) or O(mlogn), can you prove it is actually O(n+m) or propose a similar but O(n+m) algorithm?

## Solution - Binary Search

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here
        res = []
        # since answer can never be 0, n - 1 (they must be small value)
        up, down = 1, len(A) - 2
        while up + 1 < down:
            mid_row = up + (down - up)//2
            col = self.find_col(mid_row, A)
            if A[mid_row][col] < A[mid_row - 1][col]:
                down = mid_row
            elif A[mid_row][col] < A[mid_row + 1][col]:
                up = mid_row
            else:
                res = [mid_row, col]
                return res

        col = self.find_col(up, A)
        if A[up][col] > A[up - 1][col] and A[up][col] > A[up + 1][col]:
            res = [up, col]
            return res

        col = self.find_col(down, A)
        res = [down, col]
        return res

    def find_col(self, row, A):
        col = 0
        for i in range(len(A[row])):
            if A[row][i] > A[row][col]:
                col = i
        return col            
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(mlogn)**
* **Space Complexity: O(1)**

****

## Solution - Recursion

{% tabs %}
{% tab title="Python" %}
```python
DIRECTIONS = ((0, 1), (0, -1), (-1, 0), (1, 0))

class Solution:

    def findPeakII(self, A):
        return self.dfs(A, 1, len(A) - 2, 1, len(A[0]) - 2)

    def dfs(self, A, up, down, left, right):
        mid_x, mid_y = (up + down) // 2, (left + right) // 2
        x, y = mid_x, mid_y
        highest = A[x][y]

        for i in range(up, down + 1):
            if A[i][mid_y] > highest:
                highest = A[i][mid_y]
                x, y = i, mid_y
        for i in range(left, right + 1):
            if A[mid_x][i] > highest:
                highest = A[mid_x][i]
                x, y = mid_x, i

        is_peak = True
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if A[nx][ny] > A[x][y]:
                is_peak = False
                x, y = nx, ny
                break
        if is_peak:
            return [x, y]
        # serach in the pointed direction
        if up <= x < mid_x and left <= y < mid_y:
            return self.dfs(A, up, mid_x - 1, left, mid_y - 1)
        if up <= x < mid_x and mid_y < y <= right:
            return self.dfs(A, up, mid_x - 1, mid_y + 1, right)
        if mid_x < x <= down and left <= y < mid_y:
            return self.dfs(A, mid_x + 1, down, left, mid_y - 1)
        if mid_x < x <= down and mid_y < y <= right:
            return self.dfs(A, mid_x + 1, down, mid_y + 1, right)

        return []
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(m + n)**&#x20;
* **Space Complexity: O(1)**
