# Coin Change 2 740 \(M\)

## Problem

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

You can assume below:

* 0 &lt;= amount &lt;= 5000
* 1 &lt;= coin &lt;= 5000
* the number of coins is less than 500
* the answer is guaranteed to fit into signed 32-bit integer

Example

**Example1**

```text
Input: amount = 10 and coins = [10] Output: 1
```

**Example2**

```text
Input: amount = 8 and coins = [2, 3, 8]Output: 3Explanation:there are three ways to make up the amount:8 = 88 = 3 + 3 + 28 = 2 + 2 + 2 + 2
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param amount: a total amount of money amount
    @param coins: the denomination of each coin
    @return: the number of combinations that make up the amount
    """
    def change(self, amount, coins):
        # write your code here
        if not coins:
            return 0
        
        if amount == 0:
            return 1
        
        n = len(coins)
        # dp state
        # dp[i][j]: using i kinds of coins to make up j amount of money 
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # init, only one way to make up with one kind of coin
        for j in range(0, amount + 1, coins[0]):
            dp[1][j] = 1
        
        for i in range(2, n + 1):
            for j  in range(amount + 1):
                for k in range(0, j/coins[i - 1], 1):
                    dp[i][j]=+dp[i - 1][j - k * coins[i - 1]]
        
        return dp[n][amount]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

