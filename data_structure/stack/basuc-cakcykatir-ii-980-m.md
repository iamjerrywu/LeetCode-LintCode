# Basuc Calculator II 980 \(M\)

## Problem

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only **non-negative** integers, `+`, `-`, `*`, `/` operators and empty spaces . Division of integers should round off decimals.

You may assume that the given expression is always valid.

**Do not** use the `eval` built-in library function.Example

Example 1:

```text
Input:
"3+2*2"
Output:
7
```

Example 2:

```text
Input:
" 3/2 "
Output:
1
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
        num, sign = 0, '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if (not c.isdigit() and not c.isspace()) or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign =='*':
                    stack.append(stack.pop() * num)
                else:
                    # WARNING! 
                    # can't write stack.pop()//num
                    # since "//" is floor division, like -3//4 = -1 instead of 0
                    # in this case division of integers should round off decimals
                    stack.append(int(stack.pop()/num))
                sign = c 
                num = 0
        return sum(stack)
        

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

