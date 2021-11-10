# Determine Whether Matrix Can Be Obtained By Rotation (LeetCode 1886) (E)

## Problem

Given two `n x n` binary matrices `mat` and `target`, return `true`_ if it is possible to make _`mat`_ equal to _`target`_ by **rotating** _`mat`_ in **90-degree increments**, or _`false`_ otherwise._

**Example 1:**![](https://assets.leetcode.com/uploads/2021/05/20/grid3.png)

```
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/05/20/grid4.png)

```
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
```

**Example 3:**![](https://assets.leetcode.com/uploads/2021/05/26/grid4.png)

```
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
```

**Constraints:**

* `n == mat.length == target.length`
* `n == mat[i].length == target[i].length`
* `1 <= n <= 10`
* `mat[i][j]` and `target[i][j]` are either `0` or `1`.

[Discuss](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/discuss)\


## Solution - In Place Comparsion

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        can_rotate_0 = True
        can_rotate_90 = True
        can_rotate_180 = True
        can_rotate_270 = True
        
        n = len(mat)
        
        #rotate 0
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    can_rotate_0 = False
                if mat[i][j] != target[j][n - i - 1]:
                    can_rotate_90 = False
                if mat[i][j] != target[n - i - 1][n - j - 1]:
                    can_rotate_180 = False
                if mat[i][j] != target[n - j - 1][i]:
                    can_rotate_270 = False
        
        return can_rotate_0 | can_rotate_90 | can_rotate_180 | can_rotate_270
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^2)**
* **Space Complexity: O(1)**
