# Sqrt(x) (LeetCode 69) (E)

## Problem

****

Given a non-negative integer `x`, return _the square root of_ `x` _rounded down to the nearest integer_. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.

* For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

&#x20;

**Example 1:**

<pre><code>Input: x = 4
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> The square root of 4 is 2, so we return 2.</code></pre>

**Example 2:**

<pre><code>Input: x = 8
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.</code></pre>

&#x20;

**Constraints:**

* `0 <= x <= 231 - 1`



## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x + 1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if mid * mid > x:
                end = mid
            elif mid * mid < x:
                start = mid
            else:
                return mid
        if start*start > x:
            return start - 1
        if end*end > x:
            return end - 1
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

