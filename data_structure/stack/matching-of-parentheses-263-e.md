# Matching of parentheses 263 \(E\)

## Problem

## Solution

```text
Input: "()"Output: True
```

**Example 2:**

```text
Input: ")("Output: False
```

**Example 1:**

The brackets must close in the correct order, `"()"` and `"()"` are all valid but `"(]"` and `")("` are not.Example

Given a string containing just the characters `'(', ')'`, determine if the input string is valid.



### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param string: A string
    @return: whether the string is a valid parentheses
    """
    def matchParentheses(self, string):
        # write your code here
        cnt = 0
        for c in string:
            if c == '(':
                cnt+=1
            else:
                cnt-=1
            if cnt < 0:
                return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

