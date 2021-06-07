# Number of Ways to Stay in the Same Place After Some Steps II 1827 \(M\)

## Problem

You have a pointer at index 00 in an array of size arrLenarrLen.

At each step, you can move 11 position to the left, 11 position to the right in the array or stay in the same place \(The pointer should not be placed outside the array at any time\).

Given two integers stepssteps and arrLenarrLen, return the number of ways such that your pointer still at index 00 after **exactly** stepssteps steps.

Since the answer may be too large, return it **modulo** 10^9 + 7109+7.

* 1 \leq steps \leq 5001≤steps≤500
* 1 \leq arrLen \leq 10^61≤arrLen≤106

Example

**Example 1:**

```text
Input: 32Output: 4Explanation: There are 4 differents ways to stay at index 0 after 3 steps.Right, Left, StayStay, Right, LeftRight, Stay, LeftStay, Stay, Stay
```

**Example 2:**

```text
Input: 24Output: 2Explanation: There are 2 differents ways to stay at index 0 after 2 stepsRight, LeftStay, Stay
```

**Example 3:**

```text
Input: 42Output: 8
```

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
MOD = 10**9 + 7
class Solution:
    """
    @param steps: steps you can move
    @param arrLen: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    def numWays(self, steps, arrLen):
        # write your code here
        if arrLen == 1:
            return 1
        
        # calculate the farest distance you can go
        n = min(steps//2 + 1, arrLen)

        # state: dp[i][j] means how many ways you stay at j, after waking i steps
        dp = [[0] * n for _ in range(steps + 1)]

        # init
        dp[0][0] = 1

        #dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
        for i in range(1, steps + 1):
            # first point and last point need to additionally consider
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1])%MOD
            dp[i][n - 1] = (dp[i - 1][n - 1] + dp[i - 1][n - 2])%MOD

            for j in range(1, n - 1):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1])%MOD
        return dp[steps][0]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\*m\)**
* **Space Complexity: O\(n\*m\)**

## Solution - DP with strolling arrays

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

