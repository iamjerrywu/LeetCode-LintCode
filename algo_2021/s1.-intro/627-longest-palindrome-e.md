# 627 · Longest Palindrome \(E\)

## Problem

[https://www.lintcode.com/problem/627/?\_from=ladder&fromId=161](https://www.lintcode.com/problem/627/?_from=ladder&fromId=161)

### Description

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example `"Aa"` is not considered a palindrome here.

### Example

**Example 1:**

```text
"abccccdd"
Output : 7
Explanation :
One longest palindrome that can be built is "dccaccd", whose length is `7`.
```

## Approach - HashSet

### Intuition

### Algorithm

#### Step by Step

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        hash = {}
        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True
        remove = len(hash)
        if remove > 0:
            remove-=1
        return len(s) - remove
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

