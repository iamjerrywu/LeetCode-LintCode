# Decode String 575 \(M\)

## Problem

Given an expression `s` contains numbers, letters and brackets. Number represents the number of repetitions inside the brackets\(can be a string or another expression\)．Please expand expression to be a string.

Numbers can only appear in front of “\[\]”.Example

**Example1**

```text
Input: S = abc3[a]
Output: "abcaaa"
```

**Example2**

```text
Input: S = 3[2[ad]3[pf]]xyz
Output: "adadpfpfpfadadpfpfpfadadpfpfpfxyz"
```

Challenge

Can you do it without recursion?

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        
        for c in s:
            #']' is a end signal
            if c != ']':
                stack.append(c)
                continue
            strs = []
            #keep popping elements out until meet '['
            while stack and stack[-1] != '[':
                strs.append(stack.pop())
            #pop out '['
            stack.pop()
            repeats = 0
            base = 1
            #'234' = 4 * 10 ^ 0 + 3 * 10 ^ 1 + 2 * 10 ^ 2
            # stack not empty and top is a number
            while stack and stack[-1].isdigit():
                repeats+=(ord(stack.pop()) - ord('0')) * base
                base*= 10
            # first reversed, then repeat the string, finanly push back to stack
            stack.append(''.join(reversed(strs)) * repeats)
        
        return ''.join(stack)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

