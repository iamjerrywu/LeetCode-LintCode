# Number of Smooth Descent Periods of a Stock (LeetCode 2110) (M)

## Problem

****

You are given an integer array `prices` representing the daily price history of a stock, where `prices[i]` is the stock price on the `ith` day.

A **smooth descent period** of a stock consists of **one or more contiguous** days such that the price on each day is **lower** than the price on the **preceding day** by **exactly** `1`. The first day of the period is exempted from this rule.

Return _the number of **smooth descent periods**_.

&#x20;

**Example 1:**

<pre><code>Input: prices = [3,2,1,4]
<strong>Output:
</strong> 7
<strong>Explanation:
</strong> There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.</code></pre>

**Example 2:**

<pre><code>Input: prices = [8,6,7,7]
<strong>Output:
</strong> 4
<strong>Explanation:
</strong> There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.</code></pre>

**Example 3:**

<pre><code>Input: prices = [1]
<strong>Output:
</strong> 1
<strong>Explanation:
</strong> There is 1 smooth descent period: [1]</code></pre>

&#x20;

**Constraints:**

* `1 <= prices.length <= 105`
* `1 <= prices[i] <= 105`

## Solution&#x20;

<figure><img src="../../../.gitbook/assets/Screen Shot 2022-09-11 at 5.23.41 PM.png" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        p1, p2 = 0, 0
        
        ans = 0
        while p2 < len(prices):
            if p2 < len(prices) - 1 and prices[p2] - 1 == prices[p2 + 1]:
                while p2 < len(prices) - 1 and prices[p2] - 1 == prices[p2 + 1]:
                    p2+=1
                ans+=(((p2 - p1 + 1) + 1) /2)*(p2 - p1 + 1)
                p2+=1
            else:
                ans+=1
                p2+=1
            p1 = p2
        return int(ans)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

****
