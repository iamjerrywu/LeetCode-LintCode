# Palindromic Substrings (LeetCode 647) (M)

## Problem

Given a string `s`, return _the number of **palindromic substrings** in it_.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

&#x20;

**Example 1:**

```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

**Example 2:**

```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

&#x20;

**Constraints:**

* `1 <= s.length <= 1000`
* `s` consists of lowercase English letters.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            cnt+=self.cnt_palindrome(i, i, s)
            if i < len(s) - 1:
                cnt+=self.cnt_palindrome(i, i + 1, s)
        return cnt
    
    def cnt_palindrome(self, left, right, s):
        ans = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                ans+=1
                left-=1
                right+=1
            else:
                break
        return ans
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

* **Time Complexity: O(n^2)**
* **Space Complexity: O(1)**

****
