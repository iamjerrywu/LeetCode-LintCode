# Greatest Common Divisor 845 \(E\)

## Problem

Given two numbers, number `a` and number `b`. Find the `greatest common divisor` of the given two numbers.

In mathematics, the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) \(gcd\) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers.Example

**Example1**

```text
Input: a = 10, b = 15
Output: 5
Explanation:
10 % 5 == 0
15 % 5 == 0
```

**Example2**

```text
Input: a = 15, b = 30
Output: 15
Explanation:
15 % 15 == 0
30 % 15 == 0
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        # write your code here
        if a != 0:
            return self.gcd((b%a), a)
        else:
            return b
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

