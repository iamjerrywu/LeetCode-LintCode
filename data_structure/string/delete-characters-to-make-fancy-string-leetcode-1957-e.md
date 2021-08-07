# Delete Characters to Make Fancy String \(LeetCode 1957\) \(E\)

## Problem

A **fancy string** is a string where no **three** **consecutive** characters are equal.

Given a string `s`, delete the **minimum** possible number of characters from `s` to make it **fancy**.

Return _the final string after the deletion_. It can be shown that the answer will always be **unique**.

**Example 1:**

```text
Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
```

**Example 2:**

```text
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
```

**Example 3:**

```text
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
```

**Constraints:**

* `1 <= s.length <= 105`
* `s` consists only of lowercase English letters.

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def makeFancyString(self, s: str) -> str:
        cnt = 1
        ans = s[0]
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                cnt+=1
            else:
                cnt = 1
            if cnt < 3:
                ans+=s[i]
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(1\)**

