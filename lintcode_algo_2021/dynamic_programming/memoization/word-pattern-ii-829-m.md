# Word Pattern II 829 \(M\)

## Problem

Description

Given a `pattern` and a string `str`, find if `str` follows the same pattern.

Here **follow** means a full match, such that there is a [bijection](https://baike.baidu.com/item/%E5%8F%8C%E5%B0%84/942799?fr=aladdin) between a letter in `pattern` and a **non-empty** substring in `str`.\(i.e if `a` corresponds to `s`, then `b` cannot correspond to `s`. For example, given pattern = `"ab"`, str = `"ss"`, return `false`.\)

You may assume both `pattern` and `str` contains only lowercase letters.Example

**Example 1**

```text
Input:
pattern = "abab"
str = "redblueredblue"
Output: true
Explanation: "a"->"red","b"->"blue"
```

**Example 2**

```text
Input:
pattern = "aaaa"
str = "asdasdasdasd"
Output: true
Explanation: "a"->"asd"
```

**Example 3**

```text
Input:
pattern = "aabb"
str = "xyzabcxzyabc"
Output: false
```

## Solution - DFS

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        return self.is_match(pattern, str, {}, set())
    
    def is_match(self, pattern, string, mapping, used):
        # if pattern is empty, then return if string is also empty
        if not pattern:
            return not string
        
        # take first char in pattern
        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if not string.startswith(word):
                return False
            # if pattern[0] match word in string, then go on
            return self.is_match(pattern[1:], string[len(word):], mapping, used)
        
        for i in range(len(string)):
            word = string[:i + 1]
            if word in used:
                continue
            
            used.add(word)
            mapping[char] = word
            
            if self.is_match(pattern[1:], string[i + 1:], mapping, used):
                return True
            
            # track back
            del mapping[char]
            used.remove(word)
        
        return False
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

