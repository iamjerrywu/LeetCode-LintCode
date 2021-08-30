# Basic Calculator 978 \(M\)

## Problem

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open `'('` and closing parentheses `')'`, the plus `'+'` or minus sign `'-'`, **non-negative** integers and empty spaces `' '`.

You may assume that the given expression is always valid.

**Do not** use the `eval` built-in library function.Example

**Example 1**

```text
Input："1 + 1"
Output：2
```

**Example 2**

```text
Input："(1+(4+5+2)-3)+(6+8)" 
Output：23
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here
        stack = []
        res, num, sign = 0, 0, 1

        for c in s:
            if c in '1234567890':
                num = num*10 + int(c)
            elif c == '+':
                res+= sign * num
                num = 0
                sign = 1
            elif c == '-':
                res +=sign * num
                num = 0
                sign = -1
            elif c == '(':
                # save the res and sign before (operation)
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ')':
                res += sign * num
                num = 0
                # first the res inside(), should tranfer to signed before ()
                ans*=stack.pop() # the sign
                # then do either "+" or "-" with res before ()
                ans += stack.pop() # the ans before (operations)
        res += sign * num
        return res


```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

