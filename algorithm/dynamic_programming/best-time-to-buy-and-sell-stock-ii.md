# Best Time to Buy and Sell Stock II

## Problem

Given an array `prices`, which represents the price of a stock in each day.

You may complete as many transactions as you like \(ie, buy one and sell one share of the stock multiple times\). However, you may not engage in multiple transactions at the same time \(ie, if you already have the stock, you must sell it before you buy again\).

Design an algorithm to find the maximum profit.Example

**Example 1:**

```text
Input: [2, 1, 2, 0, 1]Output: 2Explanation:     1. Buy the stock on the second day at 1, and sell the stock on the third day at 2. Profit is 1.    2. Buy the stock on the 4th day at 0, and sell the stock on the 5th day at 1. Profit is 1.    Total profit is 2.
```

**Example 2:**

```text
Input: [4, 3, 2, 1]Output: 0Explanation: No transaction, profit is 0.
```

## Solution - Greedy

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

\*\*\*\*

## Solution - Peak / Valley

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
        if not prices:
            return 0
        
        peak, valley = prices[0], prices[0]
        res = 0 
        idx, n = 0, len(prices)
        while idx < n - 1:
            while idx < n - 1 and prices[idx] >= prices[idx + 1]:
                idx+=1
            valley = prices[idx]

            while idx < n - 1 and prices[idx] <= prices[idx + 1]:
                idx+=1
            peak = prices[idx]

            res+=peak - valley
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(1\)**

## Solution - DP

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

