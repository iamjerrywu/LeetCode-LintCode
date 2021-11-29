# Diagonal Traverse (LeetCode 498) (M)

## Problem

&#x20;

Given an `m x n` matrix `mat`, return _an array of all the elements of the array in a diagonal order_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg)

```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

**Example 2:**

```
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
```

&#x20;

**Constraints:**

* `m == mat.length`
* `n == mat[i].length`
* `1 <= m, n <= 104`
* `1 <= m * n <= 104`
* `-105 <= mat[i][j] <= 105`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return None
        
        m = len(mat)
        n = len(mat[0])
        
        nums = [[] for _ in range(m + n)]
        
        for i in range(m):
            for j in range(n):
                nums[i + j].append(mat[i][j])
        
        ans = []
        for i in range(m + n):
            if i % 2 == 0:
                ans.extend(nums[i][::-1])
            else:
                ans.extend(nums[i])
        return ans
        
        
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
