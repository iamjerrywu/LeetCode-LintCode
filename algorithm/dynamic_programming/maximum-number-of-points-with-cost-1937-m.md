# Maximum Number of Points with Cost 1937 \(M\)

## Problem



You are given an `m x n` integer matrix `points` \(**0-indexed**\). Starting with `0` points, you want to **maximize** the number of points you can get from the matrix.

To gain points, you must pick one cell in **each row**. Picking the cell at coordinates `(r, c)` will **add** `points[r][c]` to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows `r` and `r + 1` \(where `0 <= r < m - 1`\), picking cells at coordinates `(r, c1)` and `(r + 1, c2)` will **subtract** `abs(c1 - c2)` from your score.

Return _the **maximum** number of points you can achieve_.

`abs(x)` is defined as:

* `x` for `x >= 0`.
* `-x` for `x < 0`.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-40-26-diagram-drawio-diagrams-net.png)

```text
Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-42-14-diagram-drawio-diagrams-net.png)

```text
Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.
```

**Constraints:**

* `m == points.length`
* `n == points[r].length`
* `1 <= m, n <= 105`
* `1 <= m * n <= 105`
* `0 <= points[r][c] <= 105`

## Solution 

Suppose we have result from some previous rows `pre`. What is the result for this current row `row`?  
At a first glance, for index `i` in current row, we have:  
`cur[i] = max(pre[j] - abs(j - i) for j in range(n)) + row[i]`, but we do not need to actually compare the whole array `pre` with every index `i`, which brings O\(N ^ 2\) time for a single row.  
![image](https://assets.leetcode.com/users/images/f4a6ce8a-94a2-43f0-a915-1f38784fbd2c_1626580880.3098035.png)

For a certain index `i`, the maximum value could either come from its left, or right\(including itself\). Thus we just build two arrays, `lft, rgt`, and focus on the maximum value only coming from its left or right.

Take a look at how we build `lft`.  
Apparently, `lft[0]` is just `pre[0] + row[0]`, since there is no other values on its left.  


![image](https://assets.leetcode.com/users/images/c8d2a03c-e31b-44ae-8173-3d2b48386d94_1626580886.558323.png)

For `lft[1]`, the value is the larger one between `pre[1]` or `lft[0] - 1`, considering the index shift so we need to substract `1` from `lft[0]`.  


![image](https://assets.leetcode.com/users/images/a9e09145-ec1e-4d1c-baad-935129793211_1626580891.5653405.png)

For `lft[2]`, the value is the larger one between `pre[2]` or `lft[1] - 1`, so on so forth.

**Why we just compare pre\[2\] and lft\[1\] - 1, why its not necessary to compare lft\[0\] - 2 as well?**  
Assume we do compare: `lft[1] - 1` and `lft[0] - 2` for `index 2`  
Add `1` to each term and we have: `lft[1]`, `lft[0] - 1`.  
That is exactly the previous comparison we made for `index 1`, meaning we have already selected the maximum value for the previous index, shifting all previous candidates by 1 doenst change the result.

![image](https://assets.leetcode.com/users/images/045c5759-54ba-4189-8af4-9d8888fd8053_1626580896.5886753.png)

Build `rgt` using the same method.  


![image](https://assets.leetcode.com/users/images/97576fc5-079b-4203-883f-0b3cd7ca6fef_1626580899.9305296.png)

Now for each index `i` in `row`, all we need to do is get the larger one from `lft[i], rgt[i]`, plus `row[i]`, and that is the maximum value for this current row.  


![image](https://assets.leetcode.com/users/images/6d117416-9210-4f4a-a5e0-57ce6fe97f52_1626580904.2815344.png)

Therefore, for each row, we get `lft, rgt` from `pre`, get `cur(the next pre)` from `row, lft, rgt`, until we reach the last row.

![image](https://assets.leetcode.com/users/images/90ed4b4f-68d7-4990-860a-e7efb5030db7_1626580911.6756952.png)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = [0] * len(points[0])
        for line in points:
            for i in range(1, len(line)):
                # left side 
                dp[i] = max(dp[i],dp[i - 1] - 1)
                # right side 
                dp[-i - 1] = max(dp[-i - 1], dp[-i] - 1)
            for i in range(len(line)):
                dp[i] += line[i]
            print(dp)
        return max(dp)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

