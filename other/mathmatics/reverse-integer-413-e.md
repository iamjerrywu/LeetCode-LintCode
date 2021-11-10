# Reverse Integer 413 (E)

## Problem

Description

Reverse digits of an integer. Returns 0 when the reversed integer overflows `32-bit integer`.Example

**Example 1:**

```
Input: 123
Output: 321
```

**Example 2:**

```
Input: -123
Output: -321
```

## Solution - Mathematic&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        # write your code here
        if (n < 0 ):
            # ignore the "-" in the beginning
            ans = int(str(n)[:0:-1]) * (-1)
        else:
            ans = int(str(n)[::-1])
        if ans > 2 ** 31 - 1 or ans < -2 ** 31:
            return 0
        else:
            return ans
```
{% endtab %}

{% tab title="java" %}
```java
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

****

## Solution - String

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        # write your code here
        if n == 0:
            return 0
        
        neg = 1
        if n < 0:
            neg, n = -1, -n
        
        reverse = 0
        while n > 0:
            reverse = reverse * 10 + n%10
            n//=10
        
        reverse*= neg
        if reverse < -(1 << 31) or reverse > (1 << 31) - 1:
            return 0
        return reverse
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
