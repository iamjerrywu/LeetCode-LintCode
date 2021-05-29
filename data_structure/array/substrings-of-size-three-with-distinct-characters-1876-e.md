# Substrings of Size Three with DIstinct Characters 1876 \(E\)

## Problem

A string is **good** if there are no repeated characters.

Given a string `s`​​​​​, return _the number of **good substrings** of length **three** in_ `s`​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A **substring** is a contiguous sequence of characters in a string.

**Example 1:**

```text
Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
```

**Example 2:**

```text
Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
```

**Constraints:**

* `1 <= s.length <= 100`
* `s`​​​​​​ consists of lowercase English letters.

## Solution - Set + Queue

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        queue = collections.deque()
        unique = set()
        cnt = 0
        for i in range(len(s)):
            queue.append(s[i])
            unique.add(s[i])
            if len(queue) > 3:
                left = queue.popleft()
                if left!=queue[-1] and left != queue[-2] and left != queue[-3]:
                    unique.remove(left)
            if len(unique) == 3:
                cnt+=1
        return cnt
                
        
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

