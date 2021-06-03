# Dices Sum 20 \(M\)

## Problem

Throw `n` dices, the sum of the dices' faces is `S`. Given `n`, find the all possible value of `S` along with its probability.

You do not care about the accuracy of the result, we will help you to output results.Example

**Example 1:**

Input:

```text
n = 1
```

Output:

```text
[[1, 0.17], [2, 0.17], [3, 0.17], [4, 0.17], [5, 0.17], [6, 0.17]]
```

Explanation:

Throw one dice, the sum of the numbers facing up may be 1, 2, 3, 4, 5, 6, and the probability of each result is 0.17.

**Example 2:**

Input:

```text
n = 2
```

Output:

```text
[[2,0.03],[3,0.06],[4,0.08],[5,0.11],[6,0.14],[7,0.17],[8,0.14],[9,0.11],[10,0.08],[11,0.06],[12,0.03]]
```

Explanation:

Throw two dices, the sum of the numbers facing up may be in \[2,12\], and the probability of each result is different.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        ans = []
        
        # dp[i][j]: (n * 6n), dp means the probability that toss i times and get sum = j
        # i: how many times that index appears (n + 1)
        # j: sum (0 ~ 6 * n), total (6 * n + 1)
        dp = [[0] * (6 * n + 1)  for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, 7):
            dp[1][i] = 1/6
        
        for i in range(2, n + 1):
            for j in range(1, 6 * n + 1):
                for k in range(1, 7):
                    if j < k:
                        continue
                    dp[i][j] += dp[i - 1][j - k] / 6
        for i in range(n, 6 * n + 1):
            ans.append((i, dp[n][i]))
        
        return ans
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

