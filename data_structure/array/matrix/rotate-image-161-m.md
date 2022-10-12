# Rotate Image 161 (M)

## Problem

You are given an _n_ x _n_ 2D matrix representing an image.\
Rotate the image by `90` degrees (clockwise).Example

**Example 1：**

```
Input:[[1,2],[3,4]]
Output:[[3,1],[4,2]]
```

**Example 2:**

```
Input:[[1,2,3],[4,5,6],[7,8,9]]
Output:[[7,4,1],[8,5,2],[9,6,3]]
```

Challenge

Do it in-place.



## Solution - Copy

### Code - In-Place

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """
    def rotate(self, matrix):
        # write your code here
        if not matrix:
            return None
        if not matrix[0]:
            return []
        new_arr = []
        # copy rotation to new array
        for i in range(len(matrix[0])):
            tmp = []
            for j in range(len(matrix) - 1, -1, -1):
                tmp.append(matrix[j][i])
            new_arr.append(tmp)
        # assign new array values back to matrix
        for i in range(len(new_arr)):
            for j in range(len(new_arr[0])):
                matrix[i][j] = new_arr[i][j]
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution&#x20;

### Code - In-Place

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """
    def rotate(self, matrix):
        # write your code here
        n = len(matrix)
        for start in range(n//2):
            end = n - start - 1
            k = 0
            for _ in range(start, end):
                tmp = matrix[start][start + k]
                matrix[start][start + k] = matrix[end - k][start]
                matrix[end - k][start] = matrix[end][end - k]
                matrix[end][end - k] = matrix[start + k][end]
                matrix[start + k][end] = tmp
                k+=1
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

### Code -  Concise in-place

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        
        while left < right:
            # rotate times
            for i in range(right - left):
                top, bottom = left, right
                
                # save topleft
                top_left = matrix[top][left + i]
                
                # move bottom left to topleft
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                # move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # move top left to top right
                matrix[top + i][right] = top_left
                
            left+=1
            right-=1
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - Geometry

![](<../../../.gitbook/assets/Screen Shot 2022-02-04 at 8.10.17 PM.png>)

### Code - In-Place

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # first reverse matrix 
        matrix.reverse()
        
        # transpose matrix
        for i in range(len(matrix)):
            for j in range(i + 1, (len(matrix[i]))):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
