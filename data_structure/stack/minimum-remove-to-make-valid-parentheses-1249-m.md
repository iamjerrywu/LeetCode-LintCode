# Minimum Remove to Make Valid Parentheses 1249 (M)

## Problem



Given a string s of `'('` , `')'` and lowercase English characters.&#x20;

Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting _parentheses string_ is valid and return **any** valid string.

Formally, a _parentheses string_ is valid if and only if:

* It is the empty string, contains only lowercase characters, or
* It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
* It can be written as `(A)`, where `A` is a valid string.

**Example 1:**

```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

**Example 2:**

```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

**Example 3:**

```
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
```

**Example 4:**

```
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s[i]` is one of  `'('` , `')'` and lowercase English letters`.`

## Solution - Stack / String Builder

Stack store '(', id\_stack stores those need to be removed (either the '(' or ')')

If '(' already in there, then it can compensate the latest ')'

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stores '('
        stack = []
        # store index for those parenthese that need to be removed
        remove = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                remove.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                    remove.pop()
                else:
                    remove.append(i)
        
        ans = ''
        remove_set = set(remove)
        for i in range(len(s)):
            if i in remove_set:
                continue
            ans+=s[i]
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
  * Traverse String O(n)
  * Traver id\_stack O(i)
    * i: those id that need to be removed&#x20;
* **Space Complexity: O(n)**
  * Stack: worst case O(n)
  * id\_stack: worst case O(n)
  * list: O(n)

## Solution - Balance Calculating&#x20;

Two pass:&#x20;

* 1st traversal: Eliminate all invalid ')'&#x20;
  * Only '()' is eligible
* then reverse string
* 2nd traversal: Eliminate all invalid '('
  * Only ')(' is eligible

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = self.delete_invalid_closing(s, '(', ')')
        s = self.delete_invalid_closing(s[::-1], ')', '(')
        return s[::-1]
    
    def delete_invalid_closing(self, s, open_symbol, close_symbol):
        sb = []
        balance = 0
        for c in s:
            if c == open_symbol:
                balance+=1
            if c == close_symbol:
                if balance == 0:
                    continue
                balance-=1
            sb.append(c)
        return ''.join(sb) 
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(1)**
  *
* **Space Complexity: O(1)**
  *
