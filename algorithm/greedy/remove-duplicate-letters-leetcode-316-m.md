# Remove Duplicate Letters (LeetCode 316) (M)

## Problem

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is **the smallest in lexicographical order** among all possible results.

&#x20;

**Example 1:**

<pre><code>Input: s = "bcabc"
<strong>Output:
</strong> "abc"</code></pre>

**Example 2:**

<pre><code>Input: s = "cbacdcbc"
<strong>Output:
</strong> "acdb"</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 104`
* `s` consists of lowercase English letters.

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last = dict()
        for i, c in enumerate(s):
            last[c] = i
            
        appear = set()
        ans = []
        # if stack[-1] is larger than cur char and can added later, then pop it out (remove set as well)
        # else add to stack
        # once add to stack, record in set
        # no repeated adding (check with set)
        for i, c in enumerate(s):
            if c in appear:
                continue
            if not ans or ans[-1] < c or last[ans[-1]] < i:
                ans.append(c)
                appear.add(c)
            else:
                while ans and ans[-1] > c and last[ans[-1]] > i:
                    appear.remove(ans.pop())
                ans.append(c)
                appear.add(c)
        return ''.join(ans)
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
* **Space Complexity: O(n)**
