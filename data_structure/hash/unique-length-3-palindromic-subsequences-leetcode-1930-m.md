# Unique Length-3 Palindromic Subsequences \(LeetCode 1930\) \(M\)

## Problem

Given a string `s`, return _the number of **unique palindromes of length three** that are a **subsequence** of_ `s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once**.

A **palindrome** is a string that reads the same forwards and backwards.

A **subsequence** of a string is a new string generated from the original string with some characters \(can be none\) deleted without changing the relative order of the remaining characters.

* For example, `"ace"` is a subsequence of `"abcde"`.

**Example 1:**

```text
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
```

**Example 2:**

```text
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
```

**Example 3:**

```text
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
```

**Constraints:**

* `3 <= s.length <= 105`
* `s` consists of only lowercase English letters.

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # calculate length of string
        res = set()
        left = set()
        right = collections.Counter(s)
        
        for c in s:
            right[c]-=1
            if right[c] == 0:
                right.pop(c)
        
            for i in range(26):
                middle = chr(ord('a') + i)
                if middle in left and middle in right:
                    res.add((c, middle))
            left.add(c)
        
        return len(res)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

