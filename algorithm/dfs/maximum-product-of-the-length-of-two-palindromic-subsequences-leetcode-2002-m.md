# Maximum Product of the Length of Two Palindromic Subsequences \(LeetCode 2002\) \(M\)

## Problem

Given a string `s`, find two **disjoint palindromic subsequences** of `s` such that the **product** of their lengths is **maximized**. The two subsequences are **disjoint** if they do not both pick a character at the same index.

Return _the **maximum** possible **product** of the lengths of the two palindromic subsequences_.

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is **palindromic** if it reads the same forward and backward.

**Example 1:**![example-1](https://assets.leetcode.com/uploads/2021/08/24/two-palindromic-subsequences.png)

```text
Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.
```

**Example 2:**

```text
Input: s = "bb"
Output: 1
Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
The product of their lengths is: 1 * 1 = 1.
```

**Example 3:**

```text
Input: s = "accbcaxxcxx"
Output: 25
Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
The product of their lengths is: 5 * 5 = 25.
```

## Solution - Brute Force DFS

Find the valid subsequences, then compare every pairs to find out the maximum product of disjoints combination



{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def maxProduct(self, s: str) -> int:
        subsequences = []
        # search for valid subsequences
        self.dfs(0, s, '', set(), subsequences)
        
        ans = 0
        for i in range(len(subsequences) - 1):
            for j in range(i + 1, len(subsequences)):
                if i != j:
                    # when disjoint, they are no intersection btw two sets
                    if len(subsequences[i][1] & subsequences[j][1]) == 0:
                        ans = max(ans, subsequences[i][0] * subsequences[j][0])
        return ans
            
    def dfs(self, index, s, tmp, pos, subsequences):
        if index == len(s):
            if tmp and tmp == tmp[::-1]:
                subsequences.append([len(tmp), set(pos)])
            return
        
        pos.add(index)
        self.dfs(index + 1, s, tmp + s[index], pos, subsequences)
        pos.remove(index)
        
        self.dfs(index + 1, s, tmp, pos, subsequences)
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O\(n^2\)**
* **Space Complexity:** 

