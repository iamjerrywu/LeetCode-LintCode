# Three Divisors 1952 \(E\)

## Problem

Given an integer `n`, return `true` _if_ `n` _has **exactly three positive divisors**. Otherwise, return_ `false`.

An integer `m` is a **divisor** of `n` if there exists an integer `k` such that `n = k * m`.

**Example 1:**

```text
Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.
```

**Example 2:**

```text
Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.
```

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def isThree(self, n: int) -> bool:
        upper = int(sqrt(n))
        if n == 1:
            return False
        if n % upper != 0:
            return False
        if upper**2 != n:
            return False
        for i in range(2, upper):
            if n % i == 0:
                return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

