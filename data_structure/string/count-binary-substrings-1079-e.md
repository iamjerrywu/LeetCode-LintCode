# Count Binary Substrings 1079 \(E\)

## Problem

You are given an `m x n` binary matrix `mat` of `1`'s \(representing soldiers\) and `0`'s \(representing civilians\). The soldiers are positioned **in front** of the civilians. That is, all the `1`'s will appear to the **left** of all the `0`'s in each row.

A row `i` is **weaker** than a row `j` if one of the following is true:

* The number of soldiers in row `i` is less than the number of soldiers in row `j`.
* Both rows have the same number of soldiers and `i < j`.

Return _the indices of the_ `k` _**weakest** rows in the matrix ordered from weakest to strongest_.

**Example 1:**

```text
Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
```

**Example 2:**

```text
Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
```

**Constraints:**

* `m == mat.length`
* `n == mat[i].length`
* `2 <= n, m <= 100`
* `1 <= k <= m`
* `matrix[i][j]` is either 0 or 1.

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        cnt = []
        for i in range(len(mat)):
            cnt_s = 0
            for element in mat[i]:
                if element == 1:
                    cnt_s+=1
            cnt.append((i, cnt_s))
        
        cnt.sort(key = lambda c:(c[1], c[0]))
        res = []
        for i in range(k):
            res.append(cnt[i][0])
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(m \* n\)**
* **Space Complexity: O\(n\)**

\*\*\*\*

## Solution - group by characters

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt = 1
        appears = []
        res = 0
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                cnt+=1
            else:
                appears.append(cnt)
                cnt = 1
        appears.append(cnt)
        for i in range(len(appears) - 1):
            res+=(min(appears[i], appears[i + 1]))
        return res
            
                
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**
