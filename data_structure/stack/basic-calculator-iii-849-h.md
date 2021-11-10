# Basic Calculator III 849 (H)

## Problem

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, `'+'`, `'-'`, `'*'`, `'/'` operators, and open `'('` and closing parentheses `')'`. The integer division should **truncate toward zero**.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-231, 231 - 1]`.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

&#x20;

**Example 1:**

```
Input: s = "1+1"
Output: 2
```

**Example 2:**

```
Input: s = "6-4/2"
Output: 4
```

**Example 3:**

```
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
```

**Example 4:**

```
Input: s = "(2+6*3+5-(3*14/7+2)*5)+3"
Output: -12
```

**Example 5:**

```
Input: s = "0"
Output: 0
```

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def calculate(self, s: str) -> int:
        num, sign = 0, '+'
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            # add this recursion part dealing with expression within paranthess 
            # then rest of it is pretty the much the same as 
            elif c == '(':
                j, cnt = i, 0
                for i in range(j, len(s)):
                    if s[i] == '(':
                        cnt+=1
                    if s[i] == ')':
                        cnt-=1
                    if cnt == 0:
                        break
                num = self.calculate(s[j + 1:i])
                if i != len(s) - 1:
                    i+=1
                continue
            if not c.isdigit() or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop()/num))
                sign = c
                num = 0
            i+=1
        return sum(stack) + num
```
{% endtab %}
{% endtabs %}

* **Time Complexity: **
* **Space Complexity:**
