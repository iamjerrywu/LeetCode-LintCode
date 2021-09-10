# Backspace String Compare 1425 \(E\)

## Problem

Given two strings `S` and `T`, return if they are equal when both are typed into empty text editors. `#` means a backspace character.

1. `1 <= S.length <= 200`
2. `1 <= T.length <= 200`
3. `S` and `T` only contain lowercase letters and `'#'` characters.

Example

**Example 1:**

```text
Input: S = "ab#c", T = "ad#c"Output: trueExplanation: Both S and T become "ac".
```

**Example 2:**

```text
Input: S = "ab##", T = "c#d#"Output: trueExplanation: Both S and T become "".
```

**Example 3:**

```text
Input: S = "a##c", T = "#a#c"Output: trueExplanation: Both S and T become "c".
```

**Example 4:**

```text
Input: S = "a#c", T = "b"Output: falseExplanation: S becomes "c" while T becomes "b".
```

Challenge

Can you solve it in `O(N)` time and `O(1)` space?

## Solution - Stack

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:        
        return self.process(s) == self.process(t)
    
    def process(self, string):
        stack = []
        for c in string:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O\(n\)**
* **Space Complexity:  O\(n\)**

\*\*\*\*

## Solution - Two Pointer

{% tabs %}
{% tab title="Python" %}
```python

```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:** 

