# Multiply Strings (LeetCode 43) (M)

## Problem

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

&#x20;

**Example 1:**

```
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2:**

```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

&#x20;

**Constraints:**

* `1 <= num1.length, num2.length <= 200`
* `num1` and `num2` consist of digits only.
* Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        
        m = len(num1)
        n = len(num2)
        
        vals = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                sum_val = vals[i + j + 1] + mul
                vals[i + j] += sum_val//10
                vals[i + j + 1] = sum_val%10
                # print(vals)
        ans = ""
        for val in vals:
            if ans or val != 0:
                ans+=str(val)
        return ans if ans else "0"
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

* **Time Complexity: O(n^2)**
* **Space Complexity: O(n)**

****
