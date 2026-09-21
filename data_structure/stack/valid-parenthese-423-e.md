# Valid Parenthese 20 (E)

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

{% tab title="c++" %}
```cpp
class Solution {
public:
    bool isValid(string s) {
        // check if odd-length string
        if (s.size()%2) return false;
        
        // vector allocate contigious memory, while stack/deque use discrete chunks
        vector<char> charStack;
        for (char c : s) {
            if (c == '(') charStack.push_back(')');
            else if (c == '[') charStack.push_back(']');
            else if (c == '{') charStack.push_back('}');
            else {
                if (charStack.empty() || c != charStack.back()) return false;
                charStack.pop_back();
            }
        }
        return charStack.empty();
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
