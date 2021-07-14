# Add Strings 415 \(E\)

## Problem

Given two non-negative integers `num1` and `num2` represented as string, return the sum of `num1` and `num2`.

* The length of both num1 and num2 is &lt; 5100.
* Both num1 and num2 contains only digits 0-9.
* Both num1 and num2 does not contain any leading zero.
* You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example

**Example 1:**

```text
Input : num1 = "123", num2 = "45"Output : "168"
```

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here
        carry = 0
        index_1 = len(num1) - 1
        index_2 = len(num2) - 1
        
        res = ''
        while index_1 >= 0 or index_2 >= 0:
            val_1 = ord(num1[index_1]) - ord('0') if index_1 >= 0 else 0
            val_2 = ord(num2[index_2]) - ord('0') if index_2 >= 0 else 0
            if val_1 + val_2 + carry >= 10:
                res = str((val_1 + val_2 + carry)%10) + res
                carry = 1
            else:
                res = str(val_1 + val_2 + carry) + res
                carry = 0
            index_1-=1
            index_2-=1
        
        if carry == 1:
            res = '1' + res
        return res
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

