# leftmost Column with at Least a One (LeetCode 1428) (M)

## Problem

_(This problem is an **interactive problem**.)_

A **row-sorted binary matrix** means that all elements are `0` or `1` and each row of the matrix is sorted in non-decreasing order.

Given a **row-sorted binary matrix** `binaryMatrix`, return _the index (0-indexed) of the **leftmost column** with a 1 in it_. If such an index does not exist, return `-1`.

**You can't access the Binary Matrix directly.** You may only access the matrix using a `BinaryMatrix` interface:

* `BinaryMatrix.get(row, col)` returns the element of the matrix at index `(row, col)` (0-indexed).
* `BinaryMatrix.dimensions()` returns the dimensions of the matrix as a list of 2 elements `[rows, cols]`, which means the matrix is `rows x cols`.

Submissions making more than `1000` calls to `BinaryMatrix.get` will be judged _Wrong Answer_. Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix `mat`. You will not have access to the binary matrix directly.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/10/25/untitled-diagram-5.jpg)

```
Input: mat = [[0,0],[1,1]]
Output: 0
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/10/25/untitled-diagram-4.jpg)

```
Input: mat = [[0,0],[0,1]]
Output: 1
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2019/10/25/untitled-diagram-3.jpg)

```
Input: mat = [[0,0],[0,0]]
Output: -1
```

**Example 4:**

![](https://assets.leetcode.com/uploads/2019/10/25/untitled-diagram-6.jpg)

```
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
```

**Constraints:**

* `rows == mat.length`
* `cols == mat[i].length`
* `1 <= rows, cols <= 100`
* `mat[i][j]` is either `0` or `1`.
* `mat[i]` is sorted in non-decreasing order.

## Solution - Brute Force

{% tabs %}
{% tab title="Python" %}
```python
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        ans = float('inf')
        
        m, n = binaryMatrix.dimensions()
        
        for i in range(m):
            for j in range(n):
                if binaryMatrix.get(i, j) == 1:
                    ans = min(ans, j)
        return ans if ans != float('inf') else -1
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n \* m)**
* **Space Complexity:O(1)**

****

## Solution - Binary Search

{% tabs %}
{% tab title="Python" %}
```python
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        
        ans = float('inf')
        for i in range(m):
            index = self.binary_search(binaryMatrix, i, n)
            ans = min(ans, index)
        return ans if ans != float('inf') else -1
    
    def binary_search(self, binaryMatrix, row, n):
        start, end = 0, n - 1
        
        while start + 1 < end:
            mid = start + (end - start) //2
            if binaryMatrix.get(row, mid) == 0:
                start = mid
            else:
                end = mid
        if binaryMatrix.get(row, start) == 1:
            return start
        if binaryMatrix.get(row, end) == 1:
            return end
        return float('inf')
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(nlogm)**
* **Space Complexity: O(1)**
