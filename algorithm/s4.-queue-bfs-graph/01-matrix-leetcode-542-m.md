# 01 Matrix (LeetCode 542) (M)

## Problem

Given an `m x n` binary matrix `mat`, return _the distance of the nearest_ `0` _for each cell_.

The distance between two adjacent cells is `1`.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg)

<pre><code><strong>Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
</strong><strong>Output: [[0,0,0],[0,1,0],[0,0,0]]
</strong></code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg)

<pre><code><strong>Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
</strong><strong>Output: [[0,0,0],[0,1,0],[1,2,1]]
</strong></code></pre>

&#x20;

**Constraints:**

* `m == mat.length`
* `n == mat[i].length`
* `1 <= m, n <= 104`
* `1 <= m * n <= 104`
* `mat[i][j]` is either `0` or `1`.
* There is at least one `0` in `mat`.



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
    vector<int> dx = {0, 1, 0, -1};
    vector<int> dy = {1, 0, -1, 0};
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        vector<vector<int>> ret;
        deque<pair<int, int>> deq;
        for (int i = 0; i < mat.size(); i++) {
            vector<int> row;
            for (int j = 0; j < mat[0].size(); j++) {
                if (mat[i][j] == 0) {
                    row.push_back(0);
                    deq.push_back(pair<int, int>(i, j));
                } else {
                    row.push_back(INT_MAX);
                }
            }
            ret.push_back(row);
        }
        
        // bfs
        while(!deq.empty()) {
            pair<int, int> cur = deq.front();
            deq.pop_front();
            int val = ret[cur.first][cur.second];
            for (int i = 0; i < dx.size(); i++) {
                int new_x = cur.first + dx[i];
                int new_y = cur.second + dy[i];
                if (is_valid(new_x, new_y, ret, val)) {
                    ret[new_x][new_y] = val + 1;
                    deq.push_back(pair<int, int>(new_x, new_y));
                }
            }
        }
        return ret;
    }

private:
    bool is_valid(int new_x, int new_y, vector<vector<int>>&ret, int val) {
        if (0 <= new_x and new_x < ret.size() and 0 <= new_y and new_y < ret[0].size()) {
            if (ret[new_x][new_y] > (val + 1)) return true;
        }
        return false;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
