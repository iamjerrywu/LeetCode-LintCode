# Is Subsequences \(LeetCode392\) \(E\)

## Problem

Given two strings `s` and `t`, return `true` _if_ `s` _is a **subsequence** of_ `t`_, or_ `false` _otherwise_.

A **subsequence** of a string is a new string that is formed from the original string by deleting some \(can be none\) of the characters without disturbing the relative positions of the remaining characters. \(i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not\).

**Example 1:**

```text
Input: s = "abc", t = "ahbgdc"
Output: true
```

**Example 2:**

```text
Input: s = "axc", t = "ahbgdc"
Output: false
```

**Constraints:**

* `0 <= s.length <= 100`
* `0 <= t.length <= 104`
* `s` and `t` consist only of lowercase English letters.

 **Follow up:** Suppose there are lots of incoming `s`, say `s1, s2, ..., sk` where `k >= 109`, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?  


## Solution - Find All Subsequences

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subsequences = self.build_subsequences(t)
        if s in subsequences:
            return True
        return False
    
    def build_subsequences(self, word):
        subsequences = set([''])
        self.dfs(0, word, '', subsequences)
        return subsequences

    def dfs(self, index, word, tmp, subsequences):
        for i in range(index, len(word)):
            subsequences.add(tmp + word[i])
            self.dfs(i + 1, word, tmp + word[i], subsequences)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

{% hint style="danger" %}
Will LTE!
{% endhint %}

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - Two Pointers

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_p, t_p = 0, 0
        
        while s_p < len(s) and t_p < len(t):
            if s[s_p] == t[t_p]:
                s_p+=1
            t_p+=1
        
        return s_p == len(s)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(1\)**

