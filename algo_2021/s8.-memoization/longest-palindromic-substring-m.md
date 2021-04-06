---
description: Interval DP
---

# 200. Longest Palindromic Substring \(M\)

## Problem

[https://www.lintcode.com/problem/200/description](https://www.lintcode.com/problem/200/description)

### Description

### Example

## Approach - DP

### Intuition

### Algorithm

#### Step by Step

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""
        
        n = len(s)
        # cannot write as [[False] * 3] * 3
        # since later if modify [i][0], would change every row 1st element value 
        # dp[i][j] = True, if dp[i + 1][j - 1] is True and s[i] == s[j]
        # init dp
        dp = [[False] * n for _ in range(n)]
        
        # single char is palindrome
        for i in range(n):
            dp[i][i] = True
        # "" is also palindrome
        for i in range(1, n):
            dp[i][i - 1] = True

        start, longest = 0, 1
        # long string whether is palindromic is depend on short string
        # valid string length = 2 ~ n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and length > longest:
                    longest = length
                    start = i
        return s[start:start + longest]       
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
* **Space Complexity: O\(n^2\)**

