# Valid Parenthese 423 \(E\)

## Problem

Given a string containing just the characters `'(', ')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

The brackets must close in the correct order, `"()"` and `"()[]{}"` are all valid but `"(]"` and `"([)]"` are not. 

#### Example

**Example 1:**

```text
Input: "([)]"
Output: False
```

**Example 2:**

```text
Input: "()[]{}"
Output: True
```

#### Challenge

Use O\(n\) time, n is the number of parentheses.

## Solution

Only the latest input and the top of stack should be a pair

* i.e: input: '\(', top: '\)'

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            else: 
                if not stack or c != stack.pop():
                    return False
        return not stack

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

