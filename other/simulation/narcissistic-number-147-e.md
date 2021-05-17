# Narcissistic Number 147 \(E\)

## Problem

Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits. [See wiki](https://en.wikipedia.org/wiki/Narcissistic_number)

For example the 3-digit decimal number `153` is a narcissistic number because 153 = 13 + 53 + 33.

And the 4-digit decimal number `1634` is a narcissistic number because 1634 = 14 + 64 + 34 + 44.

Given `n`, return all narcissistic numbers with n digits.

You may assume n is smaller than 8.Example

**Example 1:**

```text
Input: 1
Output: [0,1,2,3,4,5,6,7,8,9]
```

**Example 2:**

```text
Input:  2
Output: []
Explanation: There is no Narcissistic Number with 2 digits.
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        # write your code here
        
        ans = []
        if n == 1:
            start = 0
        else: 
            start = 10 **(n-1)
        for i in range(start, 10**n):
            ref = i
            tmp = 0
            while i > 0:
                tmp +=(i%10)**(n)
                i = i//10
            if tmp == ref:
                ans.append(ref)
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

