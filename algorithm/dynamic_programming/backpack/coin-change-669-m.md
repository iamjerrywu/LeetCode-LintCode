# Coin Change 669 (M)

## Problem

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.\
It is guaranteed that the num of money will not exceed 10000.\
And the num of coins wii not exceed 500，The denomination of each coin will not exceed 100Example

**Example1**

```
Input: [1, 2, 5]11Output: 3Explanation: 11 = 5 + 5 + 1
```

**Example2**

```
Input: [2]3Output: -1
```

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        if not coins or amount == 0:
            return 0
        
        n = len(coins)
        # dp state:
        # dp[i]: the minimum required amount of coins to make up ith money
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // dp[i] i money's fewest way to contribute

        double dp[amount + 1];
        for (int i = 1; i < amount + 1; i++) {
            dp[i] = INT_MAX;
        }
        dp[0] = 0;
        for (int i = 0; i < (amount + 1); i++) {
            for (int coin : coins) {
                if ((i - coin) >= 0)
                dp[i] = min(dp[i - coin] + 1, dp[i]);
            }
        }
        if (dp[amount] != INT_MAX) return dp[amount];
        return -1;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
