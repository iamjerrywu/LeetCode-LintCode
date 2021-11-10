# Valid Parenthese 423 (E)

## Problem

Given a string containing just the characters `'(', ')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

The brackets must close in the correct order, `"()"` and `"()[]{}"` are all valid but `"(]"` and `"([)]"` are not.&#x20;

#### Example

**Example 1:**

```
Input: "([)]"
Output: False
```

**Example 2:**

```
Input: "()[]{}"
Output: True
```

#### Challenge

Use O(n) time, n is the number of parentheses.

## Solution

Only the latest input and the top of stack should be a pair

* i.e: input: '(', top: ')'

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
```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[')
                stack.add(s.charAt(i));
            else if (s.charAt(i) == ')' && (stack.isEmpty() || stack.peek() != '('))
                return false;
            else if (s.charAt(i) == '}' && (stack.isEmpty() || stack.peek() != '{'))
                return false;
            else if (s.charAt(i) == ']' && (stack.isEmpty() || stack.peek() != '['))
                return false;
            else
                stack.pop();
        }
        return stack.isEmpty();
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
