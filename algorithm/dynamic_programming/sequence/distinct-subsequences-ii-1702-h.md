# Distinct Subsequences II 1702 (H)

## Problem

Given a string `s`, count the number of distinct, non-empty subsequences of `s` .

Since the result may be large, **return the answer modulo **`109 + 7`.

**Example 1:**

```
Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
```

**Example 2:**

```
Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
```

**Example 3:**

```
Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
```

**Note:**

1. `s` contains only lowercase letters.
2. `1 <= s.length <= 2000`

## Solution - DP

### Code

{% tabs %}
{% tab title="python" %}
```python
MOD = 10 ** 9 + 7
class Solution:
    """
    @param S: The string s
    @return: The number of distinct, non-empty subsequences of S.
    """
    def distinctSubseqII(self, S):
        # Write your code here
        n = len(S)
        
        # dp[i]: means the the amount of subsequences that ends with ith character 
        dp = [0] * n

        # init: if i is the first place appeared S[i] character, then dp[i] = 1
        visited = set()
        for i in range(n):
            if S[i] not in visited:
                dp[i] = 1
            visited.add(S[i])
        
        # function: dp[i] = sigma{dp[j]}, within j to i -1, there is no S[i]
        # reason to do so, is that want to skip the duplicate subsequence
        # i.e: caba, 
        # for the last a, the previous character can be:
        # b: ba, aba, caba
        # a: aa, caa
        # c: ca (cannot be calculated, since it's already counted when processing the second a: a, ca) 
        for i in range(n):
            for j in range(i - 1, -1, -1):
               dp[i] = (dp[i] + dp[j]) % MOD
               if S[i] == S[j]:
                   break

        return sum(dp) % MOD 
        
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
