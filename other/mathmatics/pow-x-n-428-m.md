# Pow\(x, n\) 428 \(M\)

## Problem

Implement pow\(x, n\). \(n is an integer.\)

You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than `1e-3`.Example

**Example 1:**

```text
Input: x = 9.88023, n = 3Output: 964.498
```

**Example 2:**

```text
Input: x = 2.1, n = 3Output: 9.261
```

**Example 3:**

```text
Input: x = 1, n = 0Output: 1
```

Challenge

O\(_logn_\) time

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        if n < 0:
            x= 1/x
            n = -n
        
        if n%2 == 1:
            return x * self.myPow(x * x, (n - 1)/2)
        else:
            return self.myPow(x * x, n / 2)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(logn\)**
* **Space Complexity:**

