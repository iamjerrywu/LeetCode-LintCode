# Longest Valid Parentheses 193 \(M\)

## Problem

Given a string containing just the characters `'('` and `')'`, find the length of the longest valid \(well-formed\) parentheses substring.

**Example 1:**

```text
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
```

**Example 2:**

```text
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
```

**Example 3:**

```text
Input: s = ""
Output: 0
```

**Constraints:**

* `0 <= s.length <= 3 * 104`
* `s[i]` is `'('`, or `')'`.

## Solution - Stack

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity:** 
* **Space Complexity:** 

