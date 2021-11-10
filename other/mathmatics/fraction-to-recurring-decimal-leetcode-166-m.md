# Fraction to Recurring Decimal (LeetCode 166) (M)

## Problem

Given two integers representing the `numerator` and `denominator` of a fraction, return _the fraction in string format_.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return **any of them**.

It is **guaranteed** that the length of the answer string is less than `104` for all the given inputs.

**Example 1:**

```
Input: numerator = 1, denominator = 2
Output: "0.5"
```

**Example 2:**

```
Input: numerator = 2, denominator = 1
Output: "2"
```

**Example 3:**

```
Input: numerator = 2, denominator = 3
Output: "0.(6)"
```

**Example 4:**

```
Input: numerator = 4, denominator = 333
Output: "0.(012)"
```

**Example 5:**

```
Input: numerator = 1, denominator = 5
Output: "0.2"
```

&#x20;

**Constraints:**

* `-231 <= numerator, denominator <= 231 - 1`
* `denominator != 0`

Accepted167,519Submissions726,079

## Solution&#x20;

![](<../../.gitbook/assets/Screen Shot 2021-11-06 at 1.22.41 PM.png>)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        ans = ""
        
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            ans+='-'
        
        divisor = abs(numerator)
        dividend = abs(denominator)
        remainder = divisor%dividend
        ans+=str(divisor//dividend)
        
        if remainder == 0:
            return ans
        
        ans+='.'
        
        appear = {}
        while remainder != 0:
            if remainder in appear:
                index = appear[remainder]
                ans = ans[:index] + '(' + ans[index:] + ')'
                break
            appear[remainder] = len(ans)
            remainder*=10
            ans+=str(remainder//dividend)
            remainder = remainder%dividend
        return ans
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****
