# Knight Dialer (LeetCode 935) (M)

## Problem



The chess knight has a **unique movement**, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an **L**). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

![](https://assets.leetcode.com/uploads/2020/08/18/chess.jpg)

We have a chess knight and a phone pad as shown below, the knight **can only stand on a numeric cell** (i.e. blue cell).

![](https://assets.leetcode.com/uploads/2020/08/18/phone.jpg)

Given an integer `n`, return how many distinct phone numbers of length `n` we can dial.

You are allowed to place the knight **on any numeric cell** initially and then you should perform `n - 1` jumps to dial a number of length `n`. All jumps should be **valid** knight jumps.

As the answer may be very large, **return the answer modulo** `109 + 7`.

&#x20;

**Example 1:**

<pre><code>Input: n = 1
<strong>Output:
</strong> 10
<strong>Explanation:
</strong> We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
</code></pre>

**Example 2:**

<pre><code>Input: n = 2
<strong>Output:
</strong> 20
<strong>Explanation:
</strong> All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
</code></pre>

**Example 3:**

<pre><code>Input: n = 3131
<strong>Output:
</strong> 136006598
<strong>Explanation:
</strong> Please take care of the mod.
</code></pre>

&#x20;

**Constraints:**

* `1 <= n <= 5000`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def knightDialer(self, n: int) -> int:
        # dp[i][j], ith times, jth position
        dp = [[0] * 10 for _ in range(n)]
        
        for j in range(10):
            dp[0][j] = 1
            
        for i in range(1, n):
            dp[i][1] = dp[i - 1][6] + dp[i - 1][8]
            dp[i][2] = dp[i - 1][7] + dp[i - 1][9]
            dp[i][3] = dp[i - 1][4] + dp[i - 1][8]
            dp[i][4] = dp[i - 1][3] + dp[i - 1][9] + dp[i - 1][0]
            dp[i][5] = 0
            dp[i][6] = dp[i - 1][7] + dp[i - 1][1] + dp[i - 1][0]
            dp[i][7] = dp[i - 1][2] + dp[i - 1][6]
            dp[i][8] = dp[i - 1][1] + dp[i - 1][3]
            dp[i][9] = dp[i - 1][2] + dp[i - 1][4]
            dp[i][0] = dp[i - 1][4] + dp[i - 1][6]
        return sum(dp[n - 1])%(10**9 + 7)
            
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

* **Time Complexity:**
* **Space Complexity:**
