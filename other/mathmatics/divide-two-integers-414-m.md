# Divide Two Integers 414 (M)

## Problem

Divide two integers **without using multiplication, division and mod operator.**

If it will overflow(exceeding 32-bit signed integer representation range), return `2147483647`

The integer division should truncate toward zero.Example

**Example 1:**

```
Input: dividend = 0, divisor = 1Output: 0
```

**Example 2:**

```
Input: dividend = 100, divisor = 9Output: 11
```

## Solution - Brute Force (TLE)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_sign = 1 if dividend > 0 else -1
        divisor_sign = 1 if divisor > 0 else -1
        
        i = 1
        ans = 0
        while True:
            if i * abs(divisor) > abs(dividend):
                ans = i - 1
                break
            i+=1
        return ans * dividend_sign * divisor_sign
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity O(1)**

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        a, b = abs(dividend), abs(divisor)

        ans, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                ans +=1 << shift
            shift-=1
        
        if neg:
            ans = -ans
        if ans > INT_MAX:
            return INT_MAX
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(logn)**
* **Space Complexity O(1)**
