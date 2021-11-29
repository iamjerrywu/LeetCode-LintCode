# Backspace String Compare (1425) (E)

## Problem

Given two strings `S` and `T`, return if they are equal when both are typed into empty text editors. `#` means a backspace character.

1. `1 <= S.length <= 200`
2. `1 <= T.length <= 200`
3. `S` and `T` only contain lowercase letters and `'#'` characters.

Example

**Example 1:**

```
Input: S = "ab#c", T = "ad#c"Output: trueExplanation: Both S and T become "ac".
```

**Example 2:**

```
Input: S = "ab##", T = "c#d#"Output: trueExplanation: Both S and T become "".
```

**Example 3:**

```
Input: S = "a##c", T = "#a#c"Output: trueExplanation: Both S and T become "c".
```

**Example 4:**

```
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

* **Time Complexity: O(n)**
* **Space Complexity:  O(n)**

****

## Solution - Two Pointer

{% tabs %}
{% tab title="Java" %}
```python
class Solution {
    public boolean backspaceCompare(String S, String T) {
        int i = S.length() - 1, j = T.length() - 1;
        int skipS = 0, skipT = 0;

        while (i >= 0 || j >= 0) { // While there may be chars in build(S) or build (T)
            while (i >= 0) { // Find position of next possible char in build(S)
                if (S.charAt(i) == '#') {skipS++; i--;}
                else if (skipS > 0) {skipS--; i--;}
                else break;
            }
            while (j >= 0) { // Find position of next possible char in build(T)
                if (T.charAt(j) == '#') {skipT++; j--;}
                else if (skipT > 0) {skipT--; j--;}
                else break;
            }
            // If two actual characters are different
            if (i >= 0 && j >= 0 && S.charAt(i) != T.charAt(j))
                return false;
            // If expecting to compare char vs nothing
            if ((i >= 0) != (j >= 0))
                return false;
            i--; j--;
        }
        return true;
    }
}
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**&#x20;
