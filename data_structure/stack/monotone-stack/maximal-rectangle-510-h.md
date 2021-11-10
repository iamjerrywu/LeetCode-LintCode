# Maximal Rectangle 510 (H)

## Problem

Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return _its area_.

**Example 1:**![](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)

```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
```

**Example 2:**

```
Input: matrix = []
Output: 0
```

**Example 3:**

```
Input: matrix = [["0"]]
Output: 0
```

**Example 4:**

```
Input: matrix = [["1"]]
Output: 1
```

**Example 5:**

```
Input: matrix = [["0","0"]]
Output: 0
```

**Constraints:**

* `rows == matrix.length`
* `cols == matrix[i].length`
* `0 <= row, cols <= 200`
* `matrix[i][j]` is `'0'` or `'1'`.

## Solution - Brute Force

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        max_matrix_area = 0
        for up in range(n):
            for down in range(up + 1, n + 1):
                for left in range(m):
                    for right in range(left + 1, m + 1):
                        if self.is_rectangle(matrix, up, down, left, right):
                            max_matrix_area = max(max_matrix_area, (down - up) * (right - left))
        return max_matrix_area
    
    def is_rectangle(self, matrix, up, down, left, right):
        for i in range(up, down):
            for j in range(left, right):
                if not matrix[i][j]:
                    return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^6)**
  * Enumerate the up, down, left, right, and judge whether the bounded area is filled with 1
* **Space Complexity: O(1)**

****

## Solution - Monotonic Stack

For each row, update the height row and use the monotonic stack solution in problm 122

![](<../../../.gitbook/assets/Screen Shot 2021-06-17 at 12.59.17 PM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        
        max_matrix_area = 0
        for i in range(n):
            for j in range(m):
                # if true, then keep go vertical straight, height + 1
                # if not, then stop, set height = 0
                if matrix[i][j]:
                    heights[j] +=1
                else:
                    heights[j] = 0
            #update max area
            max_matrix_area = max(max_matrix_area, self.largestRectangleArea(heights))
        return max_matrix_area
        
    def largestRectangleArea(self, heights):
        # write your code here
        if not heights:
            return 0
        
        n = len(heights)
        max_area = 0
        stack = []
        for i in range(n + 1):
            # set speical value -1, for heights[n]
            value = -1 if i == n else heights[i]
            # should be ascending
            while stack and heights[stack[-1]] > value:
                top = stack.pop(-1)

                left = stack[-1] if stack else -1
                # i would be the first one smaller than cur on the right side
                width = i - left - 1
                max_area = max(max_area, width * heights[top])
            stack.append(i)
        return max_area
      
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n \* (m + m)) = O(n \* m)**
  * Traverse from top to down: O(n)
  * Update each row the height list: O(m)
  * Monotonic stack: O(m)
* **Space Complexity: O(m)**
