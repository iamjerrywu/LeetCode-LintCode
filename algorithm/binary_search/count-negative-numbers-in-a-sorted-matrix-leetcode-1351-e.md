# Count Negative Numbers in a Sorted Matrix (LeetCode 1351) (E)

## Problem

Given a `m x n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise, return _the number of **negative** numbers in_ `grid`.

&#x20;

**Example 1:**

```
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
```

**Example 2:**

```
Input: grid = [[3,2],[1,0]]
Output: 0
```

&#x20;

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 100`
* `-100 <= grid[i][j] <= 100`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for arr in grid:
            index = self.binary_search(arr)
            if index != -1:
                cnt+=len(arr) - index
        return cnt
    
    def binary_search(self, arr):
        start, end = 0, len(arr) - 1
        
        while start + 1 < end:
            mid = start + (end - start) //2
            if arr[mid] >= 0:
                start = mid
            else:
                end = mid
            
        if arr[start] < 0:
            return start
        if arr[end] < 0:
            return end
        return -1
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

* **Time Complexity: O(nlogm)**
* **Space Complexity: O(1)**

