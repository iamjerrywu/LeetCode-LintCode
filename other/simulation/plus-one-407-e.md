# Plus One 407 \(E\)

## Problem

Given a non-negative number represented as an array of digits, plus one to the number.Returns a new array.

The number is arranged according to the number of digits, with the highest digit at the top of the list.Example

**Example 1:**

```text
Input: [1,2,3]Output: [1,2,4]
```

**Example 2:**

```text
Input: [9,9,9]Output: [1,0,0,0]
```

## Solution - Simulation

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        res, carry = [], 1
        for i in range(len(digits) - 1, -1, -1):
            digit = (digits[i] + carry)%10
            carry = (digits[i] + carry)//10
            res.append(digit)
        if carry == 1:
            res.append(1)
        res.reverse()
        return res



```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity:**

