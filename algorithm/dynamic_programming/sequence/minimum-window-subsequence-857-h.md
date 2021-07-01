# Minimum Window Subsequence 857 \(H\)

## Problem

Given strings `S` and `T`, find the minimum \(contiguous\) **substring** `W` of `S`, so that `T` is a **subsequence** of `W`.

If there is no such window in `S` that covers all characters in `T`, return the empty string `""`. If there are multiple such minimum-length windows, return the one with the smallest starting index.

* All the strings in the input will only contain lowercase letters.
* The length of `S` will be in the range `[1, 20000]`.
* The length of `T` will be in the range `[1, 100]`.

Example

**Example 1:**

```text
Input：S="jmeqksfrsdcmsiwvaovztaqenprpvnbstl"，T="u"Output：""Explanation： unable to match
```

**Example 2:**

```text
Input：S = "abcdebdde"， T = "bde"Output："bcde"Explanation："bcde" is the answer and "deb" is not a smaller window because the elements of T in the window must occur in order.
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param S: a string
    @param T: a string
    @return: the minimum substring of S
    """
    def minWindow(self, S, T):
        # Write your code here
        n = len(S)
        m = len(T)
        
        # dp state:
        # dp[i][j]: the starting index that can math the first jth string in first ith subsequence
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if S[i - 1] == T[j - 1]:
                    if j == 1:
                        dp[i][j] = i
                    else:
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        start, length = 0, n + 1
        # travese again and find the minimum starting index
        for i in range(1, n + 1):
            if dp[i][m] != 0:
                if i - dp[i][m] + 1 < length:
                    start = dp[i][m] - 1
                    length = i - dp[i][m] + 1
        if length == n + 1:
            return ''
        return S[start: start + length]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* m\)**
* **Space Complexity: O\(n \* m\)**

\*\*\*\*

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

