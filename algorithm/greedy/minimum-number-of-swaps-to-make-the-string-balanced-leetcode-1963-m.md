# Minimum Number of Swaps to Make the String Balanced (LeetCode 1963) (M)

## Problem

You are given a **0-indexed** string `s` of **even** length `n`. The string consists of **exactly** `n / 2` opening brackets `'['` and `n / 2` closing brackets `']'`.

A string is called **balanced** if and only if:

* It is the empty string, or
* It can be written as `AB`, where both `A` and `B` are **balanced** strings, or
* It can be written as `[C]`, where `C` is a **balanced** string.

You may swap the brackets at **any** two indices **any** number of times.

Return _the **minimum** number of swaps to make_ `s` _**balanced**_.

**Example 1:**

```
Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".
```

**Example 2:**

```
Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][[]".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".
```

**Example 3:**

```
Input: s = "[]"
Output: 0
Explanation: The string is already balanced.
```

**Constraints:**

* `n == s.length`
* `2 <= n <= 106`
* `n` is even.
* `s[i]` is either `'['` or `']'`.
* The number of opening brackets `'['` equals `n / 2`, and the number of closing brackets `']'` equals `n / 2`.

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minSwaps(self, s: str) -> int:
        total = 0
        min_val = float('inf')
        
        for c in s:
            if c == ']':
                total-=1
            else:
                total+=1
            min_val = min(min_val, total)
        if min_val >= 0:
            return 0
        return ((-min_val) + 1)//2
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
