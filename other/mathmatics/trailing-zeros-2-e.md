# Trailing Zeros 2 \(E\)

## Problem

Given an integer `n`, calculate the number of trailing zeros in `n!`.

1 \leq n \leq 10^{18}1≤n≤10​18​​

The time complexity of your algorithm should be O\(logn\)O\(logn\)Example

**Example 1:**

Input:

```text
n = 5
```

Output:

```text
1
```

Explanation:

5! = 120, 1 trailing zero.

**Example 2:**

Input:

```text
n = 11
```

Output:

```text
2
```

Explanation:

11! = 39916800, 2 trailing zeros.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        sum = 0
        while n:
            n//=5
            sum+=n
        return sum
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

