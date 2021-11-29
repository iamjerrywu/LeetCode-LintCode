# Maximum Number of Removable Characters (LeetCode 1898) M

## Problem

You are given two strings `s` and `p` where `p` is a **subsequence** of `s`. You are also given a **distinct 0-indexed** integer array `removable` containing a subset of indices of `s` (`s` is also **0-indexed**).

You want to choose an integer `k` (`0 <= k <= removable.length`) such that, after removing `k` characters from `s` using the **first** `k` indices in `removable`, `p` is still a **subsequence** of `s`. More formally, you will mark the character at `s[removable[i]]` for each `0 <= i < k`, then remove all marked characters and check if `p` is still a subsequence.

Return _the **maximum** _ `k` _you can choose such that_ `p` _is still a **subsequence** of_ `s` _after the removals_.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

**Example 1:**

```
Input: s = "abcacb", p = "ab", removable = [3,1,0]
Output: 2
Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
"ab" is a subsequence of "accb".
If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
Hence, the maximum k is 2.
```

**Example 2:**

```
Input: s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
Output: 1
Explanation: After removing the character at index 3, "abcbddddd" becomes "abcddddd".
"abcd" is a subsequence of "abcddddd".
```

**Example 3:**

```
Input: s = "abcab", p = "abc", removable = [0,1,2,3,4]
Output: 0
Explanation: If you remove the first index in the array removable, "abc" is no longer a subsequence.
```

**Constraints:**

* `1 <= p.length <= s.length <= 105`
* `0 <= removable.length < s.length`
* `0 <= removable[i] < s.length`
* `p` is a **subsequence** of `s`.
* `s` and `p` both consist of lowercase English letters.
* The elements in `removable` are **distinct**.

## Solution - Binary Search

![](<../../.gitbook/assets/Screen Shot 2021-06-13 at 3.21.09 PM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        start, end = 0, len(removable)
        while start + 1 < end:
            mid = start + (end - start)//2
            if self.is_sub(s, p, removable, mid):
                start = mid
            else:
                end = mid
        if self.is_sub(s, p, removable, end):
            return end
        if self.is_sub(s, p, removable, start):
            return start
    
    def is_sub(self, s, p, removable, mid):
        remove = set(removable[:mid])
        s_id = p_id = 0
        while s_id < len(s) and p_id < len(p):
            if s_id in remove:
                s_id+=1
                continue
            if s[s_id] == p[p_id]:
                s_id+=1
                p_id+=1
            else:
                s_id+=1
        return p_id == len(p)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
* **Space Complexity: O(nlogn)**
