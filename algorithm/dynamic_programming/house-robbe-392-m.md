# House Robbe 392 \(M\)

## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.Example

**Example 1:**

```text
Input: [3, 8, 4]
Output: 8
Explanation: Just rob the second house.
```

**Example 2:**

```text
Input: [5, 2, 1, 3]
Output: 8
Explanation: Rob the first and the last house.
```

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        n = len(A)
        dp = [0] * (n + 1)
        dp[1] = A[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])
        return dp[n]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

## Solution - DP with Strolling Arrays

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        n = len(A)
        dp = [0] * (n + 1)
        dp[1] = A[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])
        return dp[n]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

