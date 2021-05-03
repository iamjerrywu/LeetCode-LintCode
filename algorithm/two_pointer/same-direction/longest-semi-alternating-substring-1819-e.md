# Longest Semi Alternating Substring 1819 \(E\)

## Problem

You are given a string SS of length NN containing only characters `a` and `b`. A substring \(contiguous fragment\) of SS is called a semi-alternating substring if it does not contain three identical consecutive characters. In other words, it does not contain either `aaa` or `bbb` substrings. Note that whole SS is its own substring.

Write a function, which given a string SS, returns the length of the longest semi-alternating substring of SS.

* NN is an integer within the range \[1,200\,000\]\[1,200000\];
* string SS consists only of the characters `a` and/or `b`.

Example

**Example 1**

```text
Input: "baaabbabbb"
Output: 7
Explanation: "aabbabb" is the longest semi-alternating substring.
```

**Example 2**

```text
Input: "babba"
Output: 5
Explanation: Whole S is semi-alternating.
```

**Example 3**

```text
Input: "abaaaa"
Output: 4
Explanation: "abaa" is the longest semi-alternating substring.
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: the string
    @return: length of longest semi alternating substring
    """
    def longestSemiAlternatingSubstring(self, s):
        # # write your code here
        if s is None or len(s) == 0:
            return 0
        if len(s) < 3:
            return len(s)
        
        maxLen = 1
        left = 0
        count = 1
        
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                count+=1
                if count == 3:
                    left = right - 1
                    count = 2
            else: 
                count = 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen
        
    
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

