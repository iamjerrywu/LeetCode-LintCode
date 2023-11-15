# Distinct Subsequence (LeetCode 115) (H)

## Problem



Given two strings `s` and `t`, return _the number of distinct subsequences of `s` which equals `t`_.

A string's **subsequence** is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., `"ACE"` is a subsequence of `"ABCDE"` while `"AEC"` is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.

&#x20;

**Example 1:**

<pre><code>Input: s = "rabbbit", t = "rabbit"
<strong>Output:
</strong> 3
<strong>Explanation:
</strong>As shown below, there are 3 ways you can generate "rabbit" from s.
<strong>rabb
</strong>bit
<strong>ra
</strong>bbbit
<strong>rab
</strong>bbit
</code></pre>

**Example 2:**

<pre><code>Input: s = "babgbag", t = "bag"
<strong>Output:
</strong> 5
<strong>Explanation:
</strong>As shown below, there are 5 ways you can generate "bag" from s.
<strong>ba
</strong>bgbag
<strong>ba
</strong>bgbag
<strong>b
</strong>abgbag
babgbag
babgbag
</code></pre>

&#x20;

**Constraints:**

* `1 <= s.length, t.length <= 1000`
* `s` and `t` consist of English letters.



## Solution - DFS + Memoization

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.dfs(0, 0, s, t, dict())
    def dfs(self, i, j, s, t, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if j >= len(t):
            return 1
        if i >= len(s):
            return 0
        cnt = 0
        cnt+=self.dfs(i + 1, j, s, t, memo)
        if s[i] == t[j]:
            cnt+=self.dfs(i + 1, j + 1, s, t, memo)
        memo[(i, j)] = cnt
        return cnt
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
