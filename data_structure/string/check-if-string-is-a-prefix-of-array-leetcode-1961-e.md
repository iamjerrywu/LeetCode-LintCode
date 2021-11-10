# Check If String is a Prefix of Array (LeetCode 1961) (E)

## Problem

Given a string `s` and an array of strings `words`, determine whether `s` is a **prefix string** of `words`.

A string `s` is a **prefix string** of `words` if `s` can be made by concatenating the first `k` strings in `words` for some **positive** `k` no larger than `words.length`.

Return `true`_ if _`s`_ is a **prefix string** of _`words`_, or _`false`_ otherwise_.

**Example 1:**

```
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.
```

**Example 2:**

```
Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.
```

**Constraints:**

* `1 <= words.length <= 100`
* `1 <= words[i].length <= 20`
* `1 <= s.length <= 1000`
* `words[i]` and `s` consist of only lowercase English letters.

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        start = 0
        for word in words:
            length = len(word)
            if start >= len(s):
                break
            if s[start:start + length] != word:
                return False
            start+=length
        if start < len(s):
            return False
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
