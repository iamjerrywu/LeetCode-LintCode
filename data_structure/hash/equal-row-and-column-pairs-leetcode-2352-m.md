# Equal Row and Column Pairs (LeetCode 2352) (M)

## Problem

Given a **0-indexed** `n x n` integer matrix `grid`, _return the number of pairs_ `(r`<sub>`i`</sub>`, c`<sub>`j`</sub>`)` _such that row_ `r`<sub>`i`</sub> _and column_ `c`<sub>`j`</sub> _are equal_.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg)

<pre><code><strong>Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
</strong><strong>Output: 1
</strong><strong>Explanation: There is 1 equal row and column pair:
</strong>- (Row 2, Column 1): [2,7,7]
</code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg)

<pre><code><strong>Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
</strong><strong>Output: 3
</strong><strong>Explanation: There are 3 equal row and column pairs:
</strong>- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
</code></pre>

&#x20;

**Constraints:**

* `n == grid.length == grid[i].length`
* `1 <= n <= 200`
* `1 <= grid[i][j] <= 10`<sup>`5`</sup>



## Solution

{% tabs %}
{% tab title="Python" %}
```python
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int n = grid[0].size();
        // default map implemented with black-red tree, could hash vector
        map<vector<int>, int> rowCnt;
        // get per row
        for (int i = 0; i < n; i++) {
            rowCnt[grid[i]]++;
        }

        // get per col
        int ans = 0;
        for (int j = 0; j < n; j++) {
            vector<int> col;
            col.reserve(n);
            for (int i = 0; i < n; i++) {
                col.push_back(grid[i][j]);
            }
            ans+=rowCnt[col];
        }
        return ans;   
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n\*n)**
* **Space Complexity: O(n)**

