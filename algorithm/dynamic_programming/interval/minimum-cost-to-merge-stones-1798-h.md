# Minimum Cost to Merge Stones 1798 \(H\)

## Problem

There are N piles of stones arranged in a row. The i-th pile has stones\[i\] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.

* 1 &lt;= stones.length &lt;= 100
* 2 &lt;= K &lt;= 30
* 1 &lt;= stones\[i\] &lt;= 100

Example

Example 1:

```text
Input: stones = [3,2,4,1], K = 2Output: 20Explanation: We start with [3, 2, 4, 1].We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].We merge [4, 1] for a cost of 5, and we are left with [5, 5].We merge [5, 5] for a cost of 10, and we are left with [10].The total cost was 20, and this is the minimum possible.
```

Example 1:

```text
Input: stones = [3,2,4,1], K = 3Output: -1Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
```

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param stones: 
    @param K: 
    @return: return a integer 
    """
    def mergeStones(self, stones, K):
        # write your code here
        n = len(stones)
        if (n - 1)%(K - 1) != 0:
            return -1
        
        # preprocessing
        prefix_sum = self.get_prefix_sum(stones)

        # state: dp[i][j][k] the minimum cost to merge as k piles within range(i ~ j)
        dp = [[
            [float('inf')] * (K + 1)
            for _ in range(n)
        ] for _ in range(n)]

        # init
        for i in range(n):
            dp[i][i][1] = 0

        # function:
        # dp[i][j][K] = minx(dp[i][x][K - 1] + dp[x + 1][j][1]) // for K > 1
        # dp[i][j][1] = dp[i]][j][K] + sum(stones[i....j]) // for k = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                for k in range(2, K + 1):
                    for x in range(i, j):
                        dp[i][j][k] = min(dp[i][j][k], dp[i][x][k - 1] + dp[x + 1][j][1])
                dp[i][j][1] = dp[i][j][k] + prefix_sum[j + 1] - prefix_sum[i]
        
        # ans: dp[0][n - 1][1]
        return -1 if dp[0][n - 1][1] == float('inf') else dp[0][n - 1][1]
    
    def get_prefix_sum(self, A):
        prefix_sum =[0]
        for a in A:
            prefix_sum.append(prefix_sum[-1] + a)
        return prefix_sum

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

