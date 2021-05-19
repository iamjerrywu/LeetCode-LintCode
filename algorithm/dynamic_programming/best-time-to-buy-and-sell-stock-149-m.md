# Best Time to Buy and Sell Stock 149 \(M\)

## Problem

Say you have an array for which the _i_th element is the price of a given stock on day _i_.

If you were only permitted to complete at most one transaction \(ie, buy one and sell one share of the stock\), design an algorithm to find the maximum profit.Example

**Example 1**

```text
Input: [3, 2, 3, 1, 2]
Output: 1
Explanation: You can buy at the third day and then sell it at the 4th day. The profit is 2 - 1 = 1
```

**Example 2**

```text
Input: [1, 2, 3, 4, 5]
Output: 4
Explanation: You can buy at the 0th day and then sell it at the 4th day. The profit is 5 - 1 = 4
```

**Example 3**

```text
Input: [5, 4, 3, 2, 1]
Output: 0
Explanation: You can do nothing and get nothing.
```

## Solution 

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
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

