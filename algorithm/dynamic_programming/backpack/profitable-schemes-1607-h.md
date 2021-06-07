# Profitable Schemes 1607 \(H\)

## Problem

There is a group of `n` members, and a list of various crimes they could commit. The `ith` crime generates a `profit[i]` and requires `group[i]` members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a **profitable scheme** any subset of these crimes that generates at least `minProfit` profit, and the total number of members participating in that subset of crimes is at most `n`.

Return the number of schemes that can be chosen. Since the answer may be very large, **return it modulo** `109 + 7`.

**Example 1:**

```text
Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
```

**Example 2:**

```text
Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
```

**Constraints:**

* `1 <= n <= 100`
* `0 <= minProfit <= 100`
* `1 <= group.length <= 100`
* `1 <= group[i] <= 100`
* `profit.length == group.length`
* `0 <= profit[i] <= 100`

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param G: The people in a gang.
    @param P: A profitable scheme any subset of these crimes that generates at least P profit.
    @param group: The i-th crime requires group[i] gang members to participate.
    @param profit: The i-th crime generates a profit[i].
    @return: Return how many schemes can be chosen.
    """
    def profitableSchemes(self, G, P, group, profit):
        # Write your code here.
        n = len(group)
        # dp[i][j][k]: the amount of solution, that in first ith crimes, used j people to get at least k profit
        dp = [
            [
                [0] * (P + 1)
                for _ in range(G + 1)
            ]
            for _ in range(n + 1)
        ]

        # init
        dp[0][0][0] = 1
        
        # function:
        # dp[i][j][k] = dp[i - 1][j][k] (not execut crimes[i -1])
        #             + dp[i - 1][j - groups[i-1]][k - profit[i - 1]] (execute crime[i - 1])
        # when k - profit[i - 1] < 0, then let it = 0
        for i in range(1, n + 1):
            for j in range(G + 1):
                for k in range(P + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= group[i - 1]:
                        prev_k = max(k - profit[i - 1], 0)
                        dp[i][j][k]+=dp[i - 1][j - group[i - 1]][prev_k]
        
        total = 0
        for g in range(G + 1):
            total +=dp[n][g][P]
        return total
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* G \* P\)**
  * n: crimes length
  * G: people number
  * P: minimum profit
* **Space Complexity: O\(n \* G \* P\)**

## Solution - DP with strolling arrays

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param G: The people in a gang.
    @param P: A profitable scheme any subset of these crimes that generates at least P profit.
    @param group: The i-th crime requires group[i] gang members to participate.
    @param profit: The i-th crime generates a profit[i].
    @return: Return how many schemes can be chosen.
    """
    def profitableSchemes(self, G, P, group, profit):
        # Write your code here.
        n = len(group)
        # dp[i][j][k]: the amount of solution, that in first ith crimes, used j people to get at least k profit
        dp = [
            [
                [0] * (P + 1)
                for _ in range(G + 1)
            ]
            for _ in range(2)
        ]

        # init
        dp[0][0][0] = 1
        
        # function:
        # dp[i][j][k] = dp[i - 1][j][k] (not execut crimes[i -1])
        #             + dp[i - 1][j - groups[i-1]][k - profit[i - 1]] (execute crime[i - 1])
        # when k - profit[i - 1] < 0, then let it = 0
        for i in range(1, n + 1):
            for j in range(G + 1):
                for k in range(P + 1):
                    dp[i%2][j][k] = dp[(i - 1)%2][j][k]
                    if j >= group[i - 1]:
                        prev_k = max(k - profit[i - 1], 0)
                        dp[i%2][j][k]+=dp[(i - 1)%2][j - group[i - 1]][prev_k]
        
        total = 0
        for g in range(G + 1):
            total +=dp[n%2][g][P]
        return total
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* G \* P\)**
  * n: crimes length
  * G: people number
  * P: minimum profit
* **Space Complexity: O\(G \* P\)**

