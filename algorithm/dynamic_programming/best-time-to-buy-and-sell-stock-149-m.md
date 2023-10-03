# Best Time to Buy and Sell Stock 149 (M)

## Problem

Say you have an array for which the _i_th element is the price of a given stock on day _i_.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.Example

**Example 1**

```
Input: [3, 2, 3, 1, 2]
Output: 1
Explanation: You can buy at the third day and then sell it at the 4th day. The profit is 2 - 1 = 1
```

**Example 2**

```
Input: [1, 2, 3, 4, 5]
Output: 4
Explanation: You can buy at the 0th day and then sell it at the 4th day. The profit is 5 - 1 = 4
```

**Example 3**

```
Input: [5, 4, 3, 2, 1]
Output: 0
Explanation: You can do nothing and get nothing.
```



## Solution - Two Pointer

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        n = len(prices)
        if n <= 1:
            return 0
        
        buy, sell = 0, 1
        profit = 0
        # only need to care about sell_id reach ing end, since buy_id would never surpass sell_id
        while sell < n:
            if prices[buy] > prices[sell]:
                buy = sell
                sell+=1
                continue
            profit = max(profit, prices[sell] - prices[buy])
            sell+=1
        return profit
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 1) {
            return 0;
        }
        int buyin_id = 0, sell_id = 1;
        int profit = 0;
        while (sell_id < prices.size()) {
            if (prices[buyin_id] > prices[sell_id]) {
                buyin_id = sell_id;
                sell_id++;
                continue;
            }
            profit = max(profit, prices[sell_id] - prices[buyin_id]);
            sell_id++;
        }
        return profit;
    } 
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity:**

## Solution - Greedy&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        cost = float('inf')
        start, end = 0, len(prices)
        profit = float('-inf')
        while start < end:
            cost = min(cost, prices[start])
            profit = max(profit, prices[start] - cost)
            start+=1
        return profit
```
{% endtab %}

{% tab title="C++" %}
````cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buyin = INT_MAX;
        int profit = 0;

        for (int price : prices) {
            buyin = min(buyin, price);
            profit = max(profit, price - buyin);
        }
        return profit;
    }
};
```
````
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity:**

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        n = len(prices)
    
        # dp state:
        # dp[i] = the maximum profit can get if sell stock on ith date
        dp = [0] * n
        ans = 0
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + prices[i] - prices[i - 1], prices[i] - prices[i - 1])
            ans = max(ans, dp[i])
        return ans
             
```


{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // dp[i] means the max profit you can get if sell stock at ith day
        int dp[prices.size()] = {0};
        int profit = 0;
        for (int i = 1; i < prices.size(); i++) {
            // the max can come from taking a minimum btw [0...i - 1] or the minimum price is [i - 1]
            dp[i] = max(dp[i - 1] - prices[i - 1] + prices[i], prices[i] - prices[i - 1]);
            profit = max(profit, dp[i]);
        }
    } 
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity:**
