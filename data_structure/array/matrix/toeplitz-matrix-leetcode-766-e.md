# Toeplitz Matrix (LeetCode 766) (E)

## Problem



Given an `m x n` `matrix`, return _`true` if the matrix is Toeplitz. Otherwise, return `false`._

A matrix is **Toeplitz** if every diagonal from top-left to bottom-right has the same elements.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/ex1.jpg)

```
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/ex2.jpg)

```
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
```

&#x20;

**Constraints:**

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 20`
* `0 <= matrix[i][j] <= 99`

&#x20;

**Follow up:**

* What if the `matrix` is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
* What if the `matrix` is so large that you can only load up a partial row into the memory at once?



## Solution - Group by Category

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rec = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                diff = min(i, j)
                if (i - diff, j - diff) in rec and matrix[i][j] != rec[(i - diff, j - diff)]:
                    return False
                else:
                    rec[(i - diff, j - diff)] = matrix[i][j]

        return True
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

* **Time Complexity: O(n^2)**
* **Space Complexity: O(n + m)**



## Solution - O(1) Space Check

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        # check horizontal
        for j in range(len(matrix[0])):
            if not self.check_horizontal(0, j, matrix):
                return False
        
        # check vertical
        for i in range(len(matrix)):
            if not self.check_vertical(i, 0, matrix):
                return False
        return True
    
    def check_horizontal(self, x, y, matrix):
        for k in range(min(len(matrix[0]) - y, len(matrix)) - 1):
            if matrix[x + k][y + k] != matrix[x + k + 1][y + k + 1]:
                return False
        return True
    
    def check_vertical(self, x, y, matrix):
        for k in range(min(len(matrix) - x, len(matrix[0])) - 1):
            if matrix[x + k][y + k] != matrix[x + k + 1][y + k + 1]:
                return False
        return True
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

* **Time Complexity: O(n^2)**
* **Space Complexity: O(1)**

