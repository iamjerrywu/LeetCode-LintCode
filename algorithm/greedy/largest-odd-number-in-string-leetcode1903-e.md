# Largest Odd Number in String \(LeetCode1903\) \(E\)

## Problem



You are given a string `num`, representing a large integer. Return _the **largest-valued odd** integer \(as a string\) that is a **non-empty substring** of_ `num`_, or an empty string_ `""` _if no odd integer exists_.

A **substring** is a contiguous sequence of characters within a string.

**Example 1:**

```text
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
```

**Example 2:**

```text
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
```

**Example 3:**

```text
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
```

**Constraints:**

* `1 <= num.length <= 105`
* `num` only consists of digits and does not contain any leading zeros.

## Solution - One pass

If the LSB is odd, then the whole string to integer value must be odd as well

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n, 0, -1):
            if int(num[i - 1])%2:
                return num[0:i]
        return ''
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity:**

