# Substring With At Least K Distinct Characters 1375 \(M\)

## Problem

Given a string `S` with only lowercase characters.

Return the number of substrings that contains at least `k` distinct characters.

1. 10 ≤ length\(S\) ≤ 1,000,000
2. 1 ≤ k ≤ 26

Example

**Example 1:**

```text
Input: S = "abcabcabca", k = 4
Output: 0
Explanation: There are only three distinct characters in the string.
```

**Example 2:**

```text
Input: S = "abcabcabcabc", k = 3
Output: 55
Explanation: Any substring whose length is not smaller than 3 contains a, b, c.
    For example, there are 10 substrings whose length are 3, "abc", "bca", "cab" ... "abc"
    There are 9 substrings whose length are 4, "abca", "bcab", "cabc" ... "cabc"
    ...
    There is 1 substring whose length is 12, "abcabcabcabc"
    So the answer is 1 + 2 + ... + 10 = 55.
```

## Solution - Two Pointer Brute Force

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        unique = set()
        ans = 0
        for left in range(len(s)):
            for right in range(left, len(s)):
                unique.add(s[right])
                if len(unique) >= k:
                    ans+=len(s) - right
                    unique.clear()
                    break
        return ans

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - Two Pointer 

### Code

```python
class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        unique = {}
        ans, right = 0, 0
        for left in range(len(s)):
            while len(unique) < k and right < len(s):
                unique[s[right]] = unique.get(s[right], 0) + 1
                right+=1
            if len(unique) == k:
                # because previous right already + 1, so need to + 1 here
                ans+=len(s) - right + 1
                unique[s[left]]-=1
            if unique[s[left]] == 0:
                del unique[s[left]]
        return ans

```

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(\|s\|\)**
  * The different characters amount in `s`

