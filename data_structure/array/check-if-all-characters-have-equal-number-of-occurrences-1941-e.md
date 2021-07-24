# Check if All Characters Have Equal Number of Occurrences 1941 \(E\)

## Problem



Given a string `s`, return `true` _if_ `s` _is a **good** string, or_ `false` _otherwise_.

A string `s` is **good** if **all** the characters that appear in `s` have the **same** number of occurrences \(i.e., the same frequency\).

**Example 1:**

```text
Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
```

**Example 2:**

```text
Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
```

**Constraints:**

* `1 <= s.length <= 1000`
* `s` consists of lowercase English letters.

## Solution - Dict + Array

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        cnt_list = list(cnt.values())
        for i in range(1, len(cnt_list)):
            if cnt_list[i - 1] != cnt_list[i]:
                return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - Array

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')]+=1
        for val1 in cnt:
            if val1 != 0:
                break
        for val2 in cnt:
            if val2 != 0 and val2 != val1:
                return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

