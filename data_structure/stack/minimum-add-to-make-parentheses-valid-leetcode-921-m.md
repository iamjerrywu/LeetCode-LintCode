# Minimum Add to Make Parentheses Valid (LeetCode 921) (M)

## Problem



A parentheses string is valid if and only if:

* It is the empty string,
* It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
* It can be written as `(A)`, where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

* For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(`**`(`**`)))"` or a closing parenthesis to be `"())`**`)`**`)"`.

Return _the minimum number of moves required to make_ `s` _valid_.

&#x20;

**Example 1:**

```
Input: s = "())"
Output: 1
```

**Example 2:**

```
Input: s = "((("
Output: 3
```

&#x20;

**Constraints:**

* `1 <= s.length <= 1000`
* `s[i]` is either `'('` or `')'`.



## Solution - Greedy

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        ans = 0
        for c in s:
            if c == '(':
                cnt+=1
            if c == ')':
                if cnt == 0:
                    ans+=1
                else:
                    cnt-=1
        return ans + cnt
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

