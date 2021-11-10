# Longest Palindromic Subsequence 667 (M)

## Problem

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is `1000`.Example

**Example1**

```
Input: "bbbab"
Output: 4
Explanation:
One possible longest palindromic subsequence is "bbbb".
```

**Example2**

```
Input: "bbbbb"
Output: 5
```

## Solution - Interval DP

![](<../../../.gitbook/assets/Screen Shot 2021-05-15 at 8.50.23 PM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # init state
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n - 1):
            dp[i][i + 1] = 2 if s[i] == s[i + 1] else 1
        
        for length in range(3, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                dp[start][end] = max(dp[start][end - 1], dp[start + 1][end])
                if s[start] == s[end]:
                    dp[start][end] = max(dp[start][end], dp[start + 1][end - 1] + 2 )
        return dp[0][n - 1]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^2)**
* **Space Complexity: O(n^2)**
