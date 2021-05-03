# Anagrams 171 \(M\)

## Problem

Given an array of strings, return all groups of strings that are anagrams.If a string is Anagram,there must be another string with the same letter set but different order in S.

All inputs will be in **lower-case**Example

**Example 1:**

```text
Input:["lint", "intl", "inlt", "code"]
Output:["lint", "inlt", "intl"]
```

**Example 2:**

```text
Input:["ab", "ba", "cd", "dc", "e"]
Output: ["ab", "ba", "cd", "dc"]
```

Challenge

What is Anagram?

* Two strings are anagram if they can be the same after change the order of characters

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        if not strs:
            return []
        
        dict = {}
        for str in strs:
            sort_str = ''.join(sorted(str))
            if sort_str not in dict:
                dict[sort_str] = 1
            else:
                dict[sort_str] +=1
        
        res = []
        for str in strs:
            sort_str = ''.join(sorted(str))
            if dict[sort_str] > 1:
                res.append(str)
        return res
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

