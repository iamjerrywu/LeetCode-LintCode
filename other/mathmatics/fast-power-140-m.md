# Fast Power 140 \(M\)

## Problem

Calculate the a^n \% ba​n​​%b where a, b and n are all 32bit non-negative integers.Example

For 231 % 3 = 2

For 1001000 % 1000 = 0Challenge

O\(logn\)

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        ans = 1
        while n:
            if n % 2 == 1:
                ans = (ans * a) % b
            a = (a * a) % b
            n//=2
        return ans % b
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

