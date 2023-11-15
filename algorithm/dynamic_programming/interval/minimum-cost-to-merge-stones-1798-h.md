# Minimum Cost to Merge Stones 1798 (H)

## Problem

There are N piles of stones arranged in a row. The i-th pile has stones\[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.

* 1 <= stones.length <= 100
* 2 <= K <= 30
* 1 <= stones\[i] <= 100

Example

Example 1:

```
Input: stones = [3,2,4,1], K = 2 Output: 20Explanation: We start with [3, 2, 4, 1].We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].We merge [4, 1] for a cost of 5, and we are left with [5, 5].We merge [5, 5] for a cost of 10, and we are left with [10].The total cost was 20, and this is the minimum possible.
```

Example 1:

```
Input: stones = [3,2,4,1], K = 3Output: -1Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
```

## Solution - DP

![](<../../../.gitbook/assets/Screen Shot 2021-06-08 at 5.30.50 PM.png>)

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



## Solution - Memorization

### Code

{% tabs %}
{% tab title="python" %}
```python
from sys import maxsize

class Solution:
    """
    @param stones: 
    @param K: 
    @return: return a integer 
    """
    def mergeStones(self, stones, K):
        n = len(stones)
        
        #memo[i][j][k]: means from i to j, the minimum efforts for merging stones till k piles left
        memo = [[[maxsize for _ in range(K + 1)] for _ in range(n)] for _ in range(n)]
        
        # prefix sum of the stones
        range_sum = self.get_range_sum(stones, n)
        print(range_sum)
        
        return self.memo_search(range_sum, 0, n - 1, 1, K, memo)
        
        
    def memo_search(self, range_sum, left, right, k, K, memo):
        if memo[left][right][k] != maxsize:
            return memo[left][right][k]
        
        if left == right:
            if k == 1: return 0 
            return -1 
        
        # if want to merge to final as 1 pile, need to first make stones within [left, right] become K piles
        #i.e: [3,4,5,6,7,8,9,10,11] (9), k = 3 -> [12, 21, 30] (3) -> [63] (1)
        if k == 1:
            result = self.memo_search(range_sum, left, right, K, K, memo)
            if result == -1:
                return -1
            return result + range_sum[left][right]
        
        minimum = maxsize
        # right at least should be right - k + 1
        # since [i + 1th, right] at least k - 1 
        # right - i >= k - 1
        # i <= right - k + 1 
        for i in range(left, right - k + 2):
            # emumerate split point
            # left ~ ith, 1 pile / ith + 1 ~ right, k - 1piles
            first_part = self.memo_search(range_sum, left, i, 1, K, memo)
            rest_parts = self.memo_search(range_sum, i + 1, right, k - 1, K, memo)
            if first_part == -1 or rest_parts == -1:
                continue
            minimum = min(minimum, first_part + rest_parts)
            
        if minimum == maxsize: minimum = -1 
        memo[left][right][k] = minimum
        return minimum

    # calculate range sum btw ith / jth    
    def get_range_sum(self, stones, n):
        range_sum = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            range_sum[i][i] = stones[i]
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                range_sum[i][j] = range_sum[i][j - 1] + stones[j]
        
        return range_sum
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

