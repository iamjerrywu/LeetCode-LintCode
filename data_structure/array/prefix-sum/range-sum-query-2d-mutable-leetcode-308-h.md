# Range Sum Query 2D - Mutable (LeetCode 308) (H)

## Problem

Given a 2D matrix `matrix`, handle multiple queries of the following types:

1. **Update** the value of a cell in `matrix`.
2. Calculate the **sum** of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

Implement the NumMatrix class:

* `NumMatrix(int[][] matrix)` Initializes the object with the integer matrix `matrix`.
* `void update(int row, int col, int val)` **Updates** the value of `matrix[row][col]` to be `val`.
* `int sumRegion(int row1, int col1, int row2, int col2)` Returns the **sum** of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/summut-grid.jpg)

<pre><code>Input
["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
<strong>Output
</strong>[null, 8, null, 10]
<strong>Explanation
</strong>NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e. sum of the left red rectangle)
numMatrix.update(3, 2, 2);       // matrix changes from left image to right image
numMatrix.sumRegion(2, 1, 4, 3); // return 10 (i.e. sum of the right red rectangle)</code></pre>

&#x20;

**Constraints:**

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 200`
* `-105 <= matrix[i][j] <= 105`
* `0 <= row < m`
* `0 <= col < n`
* `-105 <= val <= 105`
* `0 <= row1 <= row2 < m`
* `0 <= col1 <= col2 < n`
* At most `104` calls will be made to `sumRegion` and `update`.

## Solution - Brute Force (O(1) on Update)

{% tabs %}
{% tab title="Python" %}
```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.data = matrix
    
    def update(self, row: int, col: int, val: int) -> None:
        # O(1)   
        self.data[row][col] = val
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # O(n * m)
        sum_val = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum_val+=self.data[i][j]
        return sum_val

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

## Solution - Brute Force (O(1) on querySum)

{% tabs %}
{% tab title="Python" %}
```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.data = matrix
        self.prefix_sums = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                self.prefix_sums[i][j] = matrix[i - 1][j - 1] + self.prefix_sums[i - 1][j] + self.prefix_sums[i][j - 1] - self.prefix_sums[i - 1][j - 1]
        print(self.prefix_sums)
    def update(self, row: int, col: int, val: int) -> None:
        # O(n * m)
        ori_val = self.data[row][col]
        diff = val - ori_val
        for i in range(row + 1, len(self.data) + 1):
            for j in range(col + 1, len(self.data[0]) + 1):
                self.prefix_sums[i][j]+=diff
        self.data[row][col] = val
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # O(1)
        return self.prefix_sums[row2 + 1][col2 + 1] - self.prefix_sums[row1][col2 + 1] - self.prefix_sums[row2 + 1][col1] + self.prefix_sums[row1][col1]
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

## Solution - Segment Tree

[https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/1836821/Python-or-create-Segment-tree-for-every-row-intuitive](https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/1836821/Python-or-create-Segment-tree-for-every-row-intuitive)

{% tabs %}
{% tab title="Python" %}
```python
class SegmentTree:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.N = len(nums)
        self.tree = defaultdict(int)
        # left, right, pos
        self._create(0, self.N - 1, 0)
    
    def _create(self, l: int, r: int, pos: int) -> None:
        if l == r:
            self.tree[pos] = self.nums[l]
            return self.tree[pos]
        mid = l + (r - l) // 2
        left = self._create(l, mid, 2 * pos + 1)
        right = self._create(mid + 1, r, 2 * pos + 2)
        self.tree[pos] = left + right
        return self.tree[pos]
    
    def update(self, ql: int, qr: int, val: int, l: int, r: int, pos: int) -> None:
        if ql <= l <= r <= qr:              # Case 1 total overlap
            self.tree[pos] = val
            return self.tree[pos]
        elif ql > r or qr < l:              # Case 2 NO overlap
            return self.tree[pos]
        mid = l + (r - l) // 2              # Case 3 Partial overlap
        left = self.update(ql, qr, val, l, mid, 2 * pos + 1)
        right = self.update(ql, qr, val, mid + 1, r, 2 * pos + 2)
        self.tree[pos] = left + right
        return self.tree[pos]
    
    def query(self, ql: int, qr: int, l: int, r: int, pos: int) -> int:
        if ql <= l <= r <= qr:              # Case 1 total overlap
            return self.tree[pos]
        elif ql > r or qr < l:              # Case 2 NO overlap
            return 0
        mid = l + (r - l) // 2              # Case 3 Partial overlap
        left = self.query(ql, qr, l, mid, 2 * pos + 1)
        right = self.query(ql, qr, mid + 1, r, 2 * pos + 2)
        return left + right


class NumMatrix:
    '''
    Space complexity: 
        O(mn) we have a segment tree of size n for every column
    
    Time complexity:
        Create: O(mn) 
        Query: O(mlogn)
        Update: O(logn)
        where m is num of rows and n is num of columns
    '''
    def __init__(self, matrix: List[List[int]]):
        if matrix and matrix[0]:
            self.empty = False
            self.N = len(matrix[0])
            self.trees = [0] * len(matrix)
            for i, row in enumerate(matrix):
                self.trees[i] = SegmentTree(row)
        else:
            self.empty = True

    def update(self, row: int, col: int, val: int) -> None:
        if not self.empty:
            self.trees[row].update(col, col, val, 0, self.N - 1, 0)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.empty:
            return 0
        result = 0
        for r in range(row1, row2 + 1):
            result += self.trees[r].query(col1, col2, 0, self.N - 1, 0)
        return result
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**



****
