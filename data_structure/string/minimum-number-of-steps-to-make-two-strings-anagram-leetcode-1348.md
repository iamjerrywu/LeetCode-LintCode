# Minimum Number of Steps to Make Two Strings Anagram (LeetCode 1348)



## Problem



Given two equal-size strings `s` and `t`. In one step you can choose **any character** of `t` and replace it with **another character**.

Return _the minimum number of steps_ to make `t` an anagram of `s`.

An **Anagram** of a string is a string that contains the same characters with a different (or the same) ordering.

&#x20;

**Example 1:**

```
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
```

**Example 2:**

```
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
```

**Example 3:**

```
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
```

**Example 4:**

```
Input: s = "xxyyzz", t = "xxyyzz"
Output: 0
```

**Example 5:**

```
Input: s = "friend", t = "family"
Output: 4
```

&#x20;

**Constraints:**

* `1 <= s.length <= 50000`
* `s.length == t.length`
* `s` and `t` contain lower-case English letters only.

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff_arr = [0] * 26
        
        for c in s:
            diff_arr[ord(c) - ord('a')]+=1
        
        for c in t:
            if diff_arr[ord(c) - ord('a')] > 0:
                diff_arr[ord(c) - ord('a')]-=1
        return sum(diff_arr)
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:  O(n)**
* **Space Complexity: O(1)**
