# Longest Palindrome 627 (E)

## Problem

Description

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example `"Aa"` is not considered a palindrome here.

Assume the length of given string will not exceed `100000`.Example

**Example 1:**

```
Input : s = "abccccdd"
Output : 7
Explanation :
One longest palindrome that can be built is "dccaccd", whose length is `7`.
```

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        hash = {}
        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True
        remove = len(hash)
        if remove > 0:
            remove-=1
        return len(s) - remove
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        map<char, int> appears;
        for(char c : s) {
            appears[c]+=1;
        }
        bool has_odd = false;
        int cnt = 0;
        for (auto kv : appears) {
            if (kv.second%2) {
                has_odd = true;
                cnt+=kv.second-1;
            } else {
                cnt+=kv.second;
            }
        }
        if (has_odd) cnt+=1;
        return cnt;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
